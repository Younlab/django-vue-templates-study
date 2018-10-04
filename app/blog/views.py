from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


def index(request):
    return render(request, 'blog/index.html')


class SampleAPIView(APIView):
    def get(self, request):
        data = {
            'apple': '사과',
        }
        return Response(data)
