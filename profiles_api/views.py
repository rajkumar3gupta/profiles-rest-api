from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test Api View"""
    serializers_class = serializers.HelloSerializers
    def get(self, request, format=None):
        """REturn a list of APIVIEW features"""
        an_apiview = [
            "Uses HTTp methods as function (get, post, patch, put, delete)",
            'Is Similar to a traditional Django View',
            'Gives us the most control over our application logic',
            "Is mapped manually to urls",
        ]

        return Response({"message":"Hello!","an_apiview":an_apiview})

    def post(self, request):
        """Create a Hello message with our name """
        serializer = self.serializers_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message":message})
        else:
            return Response(
                serializer.error,
                status = status.HTTP_400_BAD_REQUEST
            )
