from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
# Create your views here.


class ReactView(APIView):

    serializer_class = ReactSerializer 

    def post(self, request):

        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

class FetchView(APIView):
    serializer_class = ReactSerializer

    def get(self, request):
        output = [{"firstname": output.firstname, "lastname": output.lastname, "email": output.email}
                  for output in React.objects.all()]
        return Response(output)