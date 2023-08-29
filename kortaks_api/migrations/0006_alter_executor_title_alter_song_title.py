# Generated by Django 4.2.4 on 2023-08-28 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kortaks_api', '0005_alter_songnumber_unique_together_songnumber_albums_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executor',
            name='title',
            field=models.CharField(db_index=True, max_length=125, unique=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(db_index=True, max_length=125, unique=True),
        ),
    ]
