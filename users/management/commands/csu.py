from django.core.management import BaseCommand
from users.models import User, UserRole


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.all().delete()

        user = User.objects.create(

            email='admin@admin',
            first_name='admin',
            is_staff=True,
            is_superuser=True,
            role=UserRole.MODERATOR
        )
        user.set_password('123qwerty')
        user.save()
