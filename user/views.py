from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

def test(request):
    return HttpResponse("This is a test version")

@api_view(['GET', 'POST'])
def demo(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message":"This is api view"})

