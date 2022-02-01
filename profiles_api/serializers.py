from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ EXAMPLE FOR SERIALIZER AND TEST APIVIEW """
    name = serializers.CharField(max_length=10)
    