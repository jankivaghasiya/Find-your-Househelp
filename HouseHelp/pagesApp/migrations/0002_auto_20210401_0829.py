# Generated by Django 3.1.5 on 2021-04-01 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagesApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helper',
            name='works',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Helper',
        ),
        migrations.DeleteModel(
            name='Works',
        ),
    ]
