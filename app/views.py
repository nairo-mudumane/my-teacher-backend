from rest_framework import APIView
from rest_framework.response import Response

class HomeView(APIView):
  def get(self,request,format=None):
    return Response({"name":"Nairo Mudumane"},status=200)