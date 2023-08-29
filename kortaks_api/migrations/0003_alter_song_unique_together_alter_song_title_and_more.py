# Generated by Django 4.2.4 on 2023-08-28 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kortaks_api', '0002_alter_song_title'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='song',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=125, unique=True),
        ),
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.RemoveField(
            model_name='song',
            name='album_number',
        ),
        migrations.CreateModel(
            name='SongNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_number', models.PositiveIntegerField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_number', to='kortaks_api.album')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song', to='kortaks_api.song')),
            ],
            options={
                'unique_together': {('album', 'album_number')},
            },
        ),
    ]
