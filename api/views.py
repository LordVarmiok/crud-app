from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from .models import Note, Comment
from .serializers import NoteSerializer, CommentSerializer
from rest_framework.decorators import api_view
from django.core.serializers.json import DjangoJSONEncoder
import json


# Create your views here.
@api_view(['GET', 'POST'])
def note_list(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return JsonResponse({"notes": serializer.data}, safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def note_details(request, id):
    if request.method == 'GET':
        note = Note.objects.filter(id=id).first()
        note_serializer = NoteSerializer(note, many=True)
        comments = Comment.objects.filter(note_origin=note).values('id', 'text', 'date_added', 'note_origin', 'author')
        # comments_serializer = json.dumps([str(value) for value in comments], cls=DjangoJSONEncoder)
        comments_serializer = json.dumps(list(comments), cls=DjangoJSONEncoder)
        # comments_serializer = CommentSerializer(comments, many=True)
        print(comments_serializer)
        print(type(comments_serializer))
    return JsonResponse({"note": {note_serializer}, "comments": [{comments_serializer}]})
    # elif request.method == 'POST':
    #     pass
    # elif request.method == 'DELETE':
    #     pass
