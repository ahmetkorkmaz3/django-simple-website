# Generated by Django 2.2.1 on 2019-05-12 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_auto_20190512_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_content',
            field=models.CharField(max_length=2000),
        ),
    ]
