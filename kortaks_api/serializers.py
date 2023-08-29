from rest_framework import serializers
from kortaks_api.models import Executor, Album, Song, SongNumber


class ExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = ['id', 'title']


class AlbumSerializer(serializers.ModelSerializer):
    executor = ExecutorSerializer()

    class Meta:
        model = Album
        fields = ['id', 'executor', 'year_of_issue']


class SongNumberSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()

    class Meta:
        model = SongNumber
        fields = ['album_number', 'album']


class SongSerializer(serializers.ModelSerializer):
    albums = SongNumberSerializer(many=True, read_only=True)

    class Meta:
        model = Song
        fields = ['id', 'title', 'albums']
