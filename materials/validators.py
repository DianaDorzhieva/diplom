from rest_framework.serializers import ValidationError
from course.models import Course
from materials.models import Materials


class Chek_words:

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        name = dict(value).get(self.field1)
        text = dict(value).get(self.field2)
        forbidden_words = ['казино', 'ставки', 'легкий заработок', 'млм', 'маркетинг', 'криптовалюта', ]
        for item in forbidden_words:
            if name.lower() == item:
                raise ValidationError(f'Нельзя использовать {item} - запрещенное слово')
            if text != None:
                if text.lower() == item:
                    raise ValidationError(f'Нельзя использовать {item} - запрещенное слово')


class Chek_name:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        name = dict(value).get(self.field)
        item_course = Course.objects.filter(name=name)
        item_materials = Materials.objects.filter(name=name)

        if item_course.exists():
            raise ValidationError(f'Курс с этим названием уже есть')
        elif item_materials.exists():
            raise ValidationError(f'Лекция с этим названием уже есть')
