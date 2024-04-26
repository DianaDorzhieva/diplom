# Generated by Django 5.0.4 on 2024-04-23 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testing_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100, verbose_name='вопрос для теста')),
                ('materials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.materials', verbose_name='материал')),
            ],
            options={
                'verbose_name': 'тест',
                'verbose_name_plural': 'тесты',
            },
        ),
    ]
