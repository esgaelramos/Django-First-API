from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

# Create your views here.

class HelloAPIView(APIView):
    """ API VIEW OF TEST """
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """ RETURN LIST PROPIETIS APIVIEW """
        an_apiview = [
            'WE USE METHODS HTTP LIKE FUNCTIONS (GET, POST, PATCH, PUT, DELETE)',
            'LIKE A TRADITIONAL VIEW',
            'BETTER CONTROL ABOUT APP LOGIC',
            'MANUAL MAPPING URLS'
        ]
        #Always we need a response in format JSON = dictionary
        return Response(({'message': 'Hello', 'an_apiview': an_apiview}))


