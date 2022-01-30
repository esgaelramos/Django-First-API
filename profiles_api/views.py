from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloAPIView(APIView):
    """ API VIEW OF TEST """
    
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
