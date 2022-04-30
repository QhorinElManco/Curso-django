from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.users.models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "name", "last_name")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # Cuando se utiliza exclude no se utiliza fields y viceversa

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data["password"])
        updated_user.save()

        return updated_user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        # data = super().to_representation(instance)
        # print(instance)
        return {
            "id": instance["id"],
            "username": instance["username"],
            "email": instance["email"],
            "password": instance["password"],
        }


"""
class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    def validate_name(self, value):
        # custom validation
        if 'developer' in value:
            raise serializers.ValidationError(
                'Error, no puede existir un usuario con ese nombre')
        return value

    def validate_email(self, value):
        # custom validation
        if value == '':
            raise serializers.ValidationError(
                'Error, tiene que validar un correo')

        return value

    def validate(self, data):
        return data

    def create(self, validated_data):
        #return self.model.objects.create(**validated_data)
        return User.objects.create(**validated_data)
    
    
    # EXPLICACION DE UPDATE MANUAL EN UN SERIALIZER SIN MODELO
    def update(self, instance, validated_data):
        print(instance)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
        
"""
