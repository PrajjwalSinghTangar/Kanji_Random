# Generated by Django 4.1 on 2022-09-06 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanji_random', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kanji',
            name='meaning',
            field=models.CharField(max_length=48, null=True),
        ),
        migrations.AlterField(
            model_name='kanji',
            name='story',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
