from rest_framework import serializers
from .models import GeneralUser, Driver

class GeneralUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = GeneralUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        generaluser = GeneralUser(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        
        password = self.validated_data['password']
        
        generaluser.set_password(password)
        generaluser.save()
        return generaluser

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['generaluser', 'license_credentials']