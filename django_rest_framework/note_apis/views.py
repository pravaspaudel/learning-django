from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import RegisterSerializer,NotesSeralizer
from rest_framework.permissions import IsAuthenticated



class RegisterView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"success":True,
                             "message":"user registered successfully",
                             "data":serializer.data},status=201)

        return Response({"success":False,
                         "message":"failed to register a user"})


class NoteView(APIView):
    permissions_classes = [IsAuthenticated]

    def post(self,request):
        serializer = NotesSeralizer(data=request.data)

        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response({"success":True,
                             "message":"note created successfully",
                             "data":serializer.data},status=201)
        return Response({"success":False,
                         "message":"failed to create a note"})