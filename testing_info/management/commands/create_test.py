from django.core.management import BaseCommand
from testing_info.models import Testing_info
import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        Testing_info.objects.all().delete()
        test_for_create = []
        with open("testing_1.json", encoding="utf-8") as f:
            test_list = json.load(f)

        for item in test_list:
            test_for_create.append(Testing_info(**item))

        Testing_info.objects.bulk_create(test_for_create)
