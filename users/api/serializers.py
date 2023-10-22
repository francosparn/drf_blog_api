from rest_framework.serializers import ModelSerializer

from users.models import User


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        # Data to be serialized
        fields = ['id', 'email', 'username', 'password']
        
    # Encrypt password
    def create(self, validated_data):
        # Get password, if "validated_data" is stored in a password variable
        password = validated_data.pop('password', None)
        # An instance is created and the validated data is taken (username, email...)
        instance = self.Meta.model(**validated_data)
        
        if password is not None:
            # Encrypt the passwor
            instance.set_password(password)
        
        # Save password to the instance
        instance.save()
        return instance


class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = User
        # Data to be serialized
        fields = ['id', 'email', 'username', 'first_name', 'last_name']
        

class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        # Data to be serialized
        fields = ['first_name', 'last_name']