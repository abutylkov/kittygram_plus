# Generated by Django 3.2 on 2022-11-29 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0005_alter_achievement_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='color',
            field=models.CharField(choices=[('Gray', 'Серый'), ('Black', 'Чёрный'), ('White', 'Белый'), ('Ginger', 'Рыжий'), ('Mixed', 'Смешанный')], max_length=16),
        ),
    ]