# Generated by Django 4.2.4 on 2023-08-28 09:59

from django.db import migrations, models
import django.db.models.deletion
import kortaks_api.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Executor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_issue', models.PositiveIntegerField(validators=[kortaks_api.models.validate_year_of_issue])),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='kortaks_api.executor')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125, unique=True)),
                ('album_number', models.PositiveIntegerField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_number', to='kortaks_api.album')),
            ],
            options={
                'unique_together': {('title', 'album'), ('album', 'album_number')},
            },
        ),
    ]