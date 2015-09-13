# -*- coding: utf8 -*-
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializer import SnippetSerializer

# Create your views here.

@api_view(['GET', 'POST']) # only allows GET and POST request
def snippet_list(request, format=None):
    """
    List all snippets or create a snippet
    """
    if request.method == 'GET': #if the user request the list of snippets
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many = True)
        return Response(serializer.data)

    elif request.method == 'POST': #if the user wants to create a snippet
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

def snip_det_temp(request, pk):
     return render(request,'snippets/snipdetail.html')

@api_view(['GET', 'PUT', 'DELETE']) # only allows GET, PUT and DELETE request
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update or delete a snippet instance.
    """

    try:
        snippet = Snippet.objects.get(pk=pk)

    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)