from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True, required=False, help_text="Provide author_id or use authenticated user.")

    class Meta:
        model = Post
        fields = ("id", "title", "content", "author", "author_id", "created_at", "updated_at")
        read_only_fields = ("id", "author", "created_at", "updated_at")

    def validate_title(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Title must not be empty.")
        return value

    def validate_content(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Content must not be empty.")
        return value

    def create(self, validated_data):
        
        request = self.context.get("request")
        user = getattr(request, "user", None)
        author_id = validated_data.pop("author_id", None)

        if user and user.is_authenticated:
            author = user
        elif author_id:
            try:
                author = User.objects.get(id=author_id)
            except User.DoesNotExist:
                raise serializers.ValidationError({"author_id": "author_id is invalid."})
        else:
            raise serializers.ValidationError({"author": "Author not provided and no authenticated user."})

        post = Post.objects.create(author=author, **validated_data)
        return post

    def update(self, instance, validated_data):
       
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.save()
        return instance

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
      
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"]
        )
        return user

    def update(self, instance, validated_data):
       
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)

        password = validated_data.get("password", None)
        if password:
            instance.set_password(password) 

        instance.save()
        return instance

    def to_representation(self, instance):
       
        return {
            "message": "User registered/updated successfully!",
            "user": {
                "id": instance.id,
                "username": instance.username,
                "email": instance.email
            }
        }
