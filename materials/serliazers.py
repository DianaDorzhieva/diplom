from rest_framework import serializers
from materials.models import Materials
from rest_framework.relations import SlugRelatedField
from course.models import Course
from materials.validators import Chek_words, Chek_name


class MaterialsSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())

    class Meta:
        model = Materials
        fields = '__all__'
        validators = [Chek_words(field1='name', field2='text'), Chek_name(field='name')]




