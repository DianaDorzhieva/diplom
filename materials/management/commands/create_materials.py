from django.core.management import BaseCommand
from materials.models import Materials
import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        Materials.objects.all().delete()
        materials_for_create = []
        with open("materials.json", encoding="utf-8") as f:
            materials_list = json.load(f)

        for item in materials_list:
            materials_for_create.append(Materials(**item))

        Materials.objects.bulk_create(materials_for_create)
