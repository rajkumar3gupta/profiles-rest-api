from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import HelloSerializers


class HelloApiView(APIView):
    """Test Api View"""
    serializer_class = HelloSerializers
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
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Partially updating an object"""
        return Response({'methode':"PATCH"})

    def delete(self, request, pk=None):
        """Delete an Object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = HelloSerializers

    def list(self, request):
        """Return a Hello Message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update',
            'Automatically maps to URLs using Routers',
            'provides more functionality with less code',
        ]
        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self, request):
        """Create a new Hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )

    def retrive(self, request, pk=None):
        """Handle getting an object by it's ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Updating an Object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Updating spacific part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Removing an object"""
        return Response({'http_method':'DELETE'})
