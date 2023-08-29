from django.urls import path
from kortaks_api.views import *


urlpatterns = [
    path('executors/', view_executors),
    path('executor/<slug:executor>/', view_executor, name='view_executor'),
    path('albums/', view_albums),
    path('album/<int:pk>/', view_album),
    path('songs/', view_songs),
    path('song/<slug:song>/', view_song, name='view_song')
]
