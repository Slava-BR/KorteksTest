from django.contrib import admin
from kortaks_api.models import Album, Song, Executor, SongNumber

# Register your models here.
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Executor)
admin.site.register(SongNumber)
