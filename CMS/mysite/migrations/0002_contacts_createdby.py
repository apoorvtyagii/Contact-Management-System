# Generated by Django 3.1.7 on 2022-04-14 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='createdby',
            field=models.EmailField(default='f', max_length=100),
            preserve_default=False,
        ),
    ]
