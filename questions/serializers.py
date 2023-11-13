from django.conf import settings
from rest_framework import serializers

from django.contrib.auth.models import Group, User

from questions.models import Answers, Questions


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model= Group
        fields = ('id','name')


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