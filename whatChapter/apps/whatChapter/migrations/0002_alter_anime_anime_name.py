# Generated by Django 3.2.12 on 2021-06-24 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("whatChapter", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="anime",
            name="anime_name",
            field=models.CharField(max_length=255),
        )
    ]
