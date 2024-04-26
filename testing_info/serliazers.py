from rest_framework import serializers
from testing_info.models import Testing_info, Answer_user


class Testing_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testing_info
        fields = ('question', 'id', 'materials_id')


class Answer_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer_user
        fields = '__all__'
