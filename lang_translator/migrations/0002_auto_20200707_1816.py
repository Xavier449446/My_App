# Generated by Django 3.0.7 on 2020-07-07 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lang_translator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio',
            field=models.FileField(upload_to='images/'),
        ),
    ]
