from django.conf import settings
from rest_framework import serializers

from django.contrib.auth.models import Group, User

from questions.models import Answers, GroupsQuestions, Questions



class GroupsQuestionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupsQuestions
        fields = ['url', 'id', 'name', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    question_group = GroupsQuestionsSerializer(source='groups_question', many=True)

    class Meta:
        model = Group
        fields = ['url', 'id', 'name', 'is_boss', 'question_group']
        # fields = ['url', 'id', 'name', 'is_boss', 'question_groups', 'groups_question']



class UserSerializer(serializers.HyperlinkedModelSerializer):

    full_name = serializers.CharField(source='get_full_name')
    # user_group = GroupSerializer(source='groups', many=True)

    class Meta:
        model = User
        fields = ['url', 'first_name', 'last_name', 'full_name', 'username', 'email', 'is_active', 'groups'] #, 'user_group']
        depth = 2

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.is_superuser:
            representation['admin'] = True
        return representation















class AnswersListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answers
        fields = '__all__'



class QuestionsSerializer(serializers.ModelSerializer):

    # answer_questions = AnswersListSerializer(read_only=True, many=True)
    # groups_questions = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    # answer_questions = serializers.SlugRelatedField(slug_field="description", read_only=True, many=True)

    class Meta:
        model = Questions
        fields = ('id',) #('description', 'in_active', 'image') #, 'groups_questions', 'answer_questions')