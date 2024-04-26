from django.core.management import BaseCommand
from course.models import Course
import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        Course.objects.all().delete()
        course_for_create = []
        with open("course.json", encoding="utf-8") as f:
            course_list = json.load(f)

        for item in course_list:
            course_for_create.append(Course(**item))

        Course.objects.bulk_create(course_for_create)
