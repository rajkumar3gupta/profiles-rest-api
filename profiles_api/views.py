from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """REturn a list of APIVIEW features"""
        an_apiview = [
            "Uses HTTp methods as function (get, post, patch, put, delete)",
            'Is Similar to a traditional Django View',
            'Gives us the most control over our application logic',
            "Is mapped manually to urls",
        ]

        return Response({"message":"Hello!","an_apiview":an_apiview})

    
