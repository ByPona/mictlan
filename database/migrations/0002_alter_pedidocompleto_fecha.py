# Generated by Django 4.0.5 on 2022-06-20 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidocompleto',
            name='fecha',
            field=models.CharField(max_length=30),
        ),
    ]
