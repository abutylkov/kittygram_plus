# Generated by Django 3.2 on 2022-11-29 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0004_alter_achievement_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='name',
            field=models.CharField(default='разбил вазу', max_length=64),
            preserve_default=False,
        ),
    ]
