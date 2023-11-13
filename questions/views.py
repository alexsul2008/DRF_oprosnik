from random import shuffle
from django.contrib.auth.models import Group, User
from django.db.models.query import QuerySet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from rest_framework.renderers import TemplateHTMLRenderer

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin



from questions.serializers import QuestionsSerializer
from questions.models import Answers, GroupsQuestions, Questions


# def index(request):
#     return render(request, 'registration/login.html')


    


def random_question(array):
    """Перемешать список"""
    shuffle(array)
    return array


def usedGroup(user):
    """
	Определение Group user и создание списка вопросов определенных для Group user
	:param user:
	:return:
	"""
    user_group = Group.objects.all()
    if (user.is_superuser or user_group.filter(user=user, is_boss=True)):
        """Для суперпользователя и группы с атрибутом is_boss все вопросы в списке"""
        current_user_group = user_group.values()

        arrayQuestions = Questions.objects.filter(Q(in_active=True) & Q(groups_questions__in_active=True)) \
            .values_list('id', flat=True).distinct()
    else:
        """Для зарегистрированного user определяем список вопросов согласно групповой принадлежности"""
        current_user_group = user_group.filter(user=user).values_list('id', flat=True)[0]
        user_list_questions_groups = GroupsQuestions.objects.filter(groups=current_user_group, in_active=True).values_list('id', flat=True)
        arrayQuestions = Questions.objects.filter(in_active=True, groups_questions__in=list(user_list_questions_groups)) \
            .values_list('id', flat=True).distinct()

    return current_user_group, arrayQuestions


# class QuestionsAPIView(LoginRequiredMixin, ListAPIView):
class QuestionsAPIView(viewsets.ModelViewSet):
# class QuestionsAPIView(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = QuestionsSerializer
    queryset = Questions.objects.all()
    
    def get_queryset(self):

        print(self.queryset)
        queryset = self.queryset

        current_group_user = Group.objects.filter(user=self.request.user).values_list('id', flat=True)[0]
        print(current_group_user)
        user_list_questions_groups = GroupsQuestions.objects.filter(groups=current_group_user, in_active=True).values_list('id', flat=True)

        # arrayQuestions = Questions.objects.filter(in_active=True, groups_questions__in=list(user_list_questions_groups)) \
        #     .values_list('id', flat=True).distinct()

        
        if isinstance(queryset, QuerySet):
            queryset = queryset.filter(in_active=True, groups_questions__in=list(user_list_questions_groups)).values('id').distinct()

            print(queryset)
        return queryset
    

    # def get(self, request, *args, **kwargs):
        
    #     current_group_user = Group.objects.filter(user=request.user).values_list('id', flat=True)[0]
    #     user_list_questions_groups = GroupsQuestions.objects.filter(groups=current_group_user, in_active=True).values_list('id', flat=True)
    #     lsts = Questions.objects.filter(in_active=True, groups_questions__in=list(user_list_questions_groups)).values('id').distinct()

    #     print(lsts)

    #     friends_ids = [lst['id'] for lst in lsts]

    #     print(friends_ids)
    #     return Response({'questions': QuestionsSerializer(lsts).data})



# class QuestionsAPIView(APIView):

#     def get(self, request):
#         # lst = Questions.objects.all()
#         lst = Questions.objects.all().values()
#         # print(lst)
#         return Response({'questions': QuestionsSerializer(lst, many=True).data})
#         # lst_data = QuestionsSerializer(lst, many=True, context={'request': request})
#         # data = lst_data.data
#         # return Response({"data":data})

#     # def get(self, request):
#     #     lst = Questions.objects.all().values()
#         # return Response({'questions': QuestionsSerializer(lst, many=True).data})
    
#     def post(self, request):

#         serialaizer = QuestionsSerializer(data=request.data)
#         serialaizer.is_valid(raise_exception=True)
#         serialaizer.save()

#         return Response({'question': serialaizer.data})

#         # question_new = Questions.objects.create(
#         #     description = request.data['description'],
#         #     image = request.data['image'],
#         #     in_active = request.data['in_active']
#         # )
#         # return Response({'question': QuestionsSerializer(question_new).data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Метод PUT не определен'})
        
#         try:
#             isinstance = Questions.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Объект не найден'})
        
#         serialaizer = QuestionsSerializer(data=request.data, instance=isinstance)
#         serialaizer.is_valid(raise_exception=True)
#         serialaizer.save()
#         return Response({'question': serialaizer.data})
        



# class QuestionsAPIView(generics.ListAPIView):
#     queryset = Questions.objects.all()
#     serializer_class = QuestionsSerializer