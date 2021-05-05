from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
    """Serializer a name fields for testing our APIViews"""
    name = serializers.CharField(max_length = 10)