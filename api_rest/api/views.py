from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def test_endpoint(request):
    return JsonResponse({'foo': 'bar'})
