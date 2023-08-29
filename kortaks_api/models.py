from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


def validate_year_of_issue(value):
    if value <= 1960 or value >= int(datetime.now().year):
        raise ValidationError(
            'year is invalid',
            params={'value': value},
        )


class Executor(models.Model):
    title = models.CharField(max_length=125, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('view_executor', kwargs={'executor': self.title})

    def __str__(self):
        return self.title


class Album(models.Model):
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, related_name='album')
    year_of_issue = models.PositiveIntegerField(validators=[validate_year_of_issue])

    def __str__(self):
        return f'Executor:{self.executor.title} - {self.pk}'


class Song(models.Model):
    title = models.CharField(max_length=125, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('view_song', kwargs={'song': self.title})

    def __str__(self):
        return self.title


class SongNumber(models.Model):
    albums = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='albums')
    album_number = models.PositiveIntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_number')

    class Meta:
        unique_together = (('album', 'album_number'), ('albums', 'album'))

    def __str__(self):
        return "%d: %s" % (self.album_number, str(self.album))
