# Generated by Django 3.0.8 on 2020-07-26 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journalbook',
            name='user',
        ),
        migrations.DeleteModel(
            name='JournaEntry',
        ),
        migrations.DeleteModel(
            name='JournalBook',
        ),
    ]