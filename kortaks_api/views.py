from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from kortaks_api.models import *
from kortaks_api.serializers import ExecutorSerializer, AlbumSerializer, SongSerializer


@api_view(['GET'])
@csrf_exempt
def view_executors(request):
    snippets = Executor.objects.all()
    serializer = ExecutorSerializer(snippets, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@csrf_exempt
def view_executor(request, executor):
    snippets = Executor.objects.filter(slug=executor)
    serializer = ExecutorSerializer(snippets, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@csrf_exempt
def view_albums(request):
    snippets = Album.objects.all()
    serializer = AlbumSerializer(snippets, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@csrf_exempt
def view_album(request, pk):
    snippets = Album.objects.filter(pk=pk)
    serializer = AlbumSerializer(snippets, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@csrf_exempt
def view_songs(request):
    snippets = Song.objects.all()
    serializer = SongSerializer(snippets, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@csrf_exempt
def view_song(request, song):
    snippets = Song.objects.filter(slug=song)
    serializer = SongSerializer(snippets, many=True)
    return JsonResponse(serializer.data, safe=False)
