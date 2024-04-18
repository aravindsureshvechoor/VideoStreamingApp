from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core import exceptions

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model  = User
        fields = '__all__'

    def validate(self, data):
        password     = data.get('password')
        re_password  = data.get('confirm_password')
        if password != re_password:
            raise serializers.ValidationError("Passwords do not match.")
        
        return data
        
    def create(self,validated_data):
        user = User.objects.create_user(
            email      = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name  = validated_data['last_name'],
            user_name  = validated_data['user_name'],
            password   = validated_data['password']
        )

        return user






