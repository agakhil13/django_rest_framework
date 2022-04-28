from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'username' : 'admin',
            'years_active' : 10
        }
        return Response(data)