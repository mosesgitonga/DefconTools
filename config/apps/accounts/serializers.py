from rest_framework import serializers 
from .models import User 

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = user 
        fields = ['email', 'username', 'password']

    class create(self, validated_data):
        role = 'hacker' if User.objects.exists() else 'root'

        user = User(
            username = validated_data['username'],
            email = validated_data['email'],
            role=role
        )
        user.set_password(validated_data['password'])
        user.save()
        return user 
        