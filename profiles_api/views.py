from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test APIView. Defines application logic for the endpoint."""

    def get(self, request, format=None):
        """Returs a list of APIView features"""
        an_apiview = [
            'Users HTTP methods as functionsm(get, post, patch, put, delete)',
            'Is simular to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response(
        {
        'message': 'Hello',
        'an_apiview': an_apiview })
