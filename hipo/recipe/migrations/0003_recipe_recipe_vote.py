# Generated by Django 2.2.1 on 2019-05-11 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_recipe_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_vote',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=30),
        ),
    ]