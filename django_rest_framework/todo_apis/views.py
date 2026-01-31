from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

class todoViews(APIView):

    def get(self,request):
        todos = Todo.objects.all()

        serilazers = TodoSerializer(todos,many=True)

        return Response(serilazers.data)

    def post(self,request):
        serlizer = TodoSerializer(data=request.data)

        if serlizer.is_valid():
            serlizer.save()
            return Response({"message":"todo created successfully"},status=201)

        return Response(serlizer.errors,status=400)
    
    def delete(self,request,id):
        todo = get_object_or_404(Todo,id=id)

