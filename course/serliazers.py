from rest_framework import serializers
from course.models import Course
from materials.validators import Chek_words, Chek_name


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        validators = [Chek_words(field1='name', field2='text'), Chek_name(field='name')]
