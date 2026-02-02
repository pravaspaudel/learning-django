from django.contrib.auth.models import User
from rest_framework import serializers
from .models import NoteModel

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)


class NotesSeralizer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source="author.username")
    class Meta:
        model = NoteModel
        fields = ['id','title','content','author','created_at']


    def create(self,validated_data):
        return NoteModel.objects.create(**validated_data)