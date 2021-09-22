from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerilizers(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'password2']
        extra_kwargs = {'password' : {'write_only' : True,}}