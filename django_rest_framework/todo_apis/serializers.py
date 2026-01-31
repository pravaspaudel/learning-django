from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
    
    def create(self,validated_data):
        todo = Todo.objects.create(
            task=validated_data["task"],
            description=validated_data["description"],
        )
        return todo



