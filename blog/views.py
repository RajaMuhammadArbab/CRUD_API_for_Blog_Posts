from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from . import services

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("title", "content")
    ordering_fields = ("created_at", "updated_at", "title")

    def get_queryset(self):
        
        return services.get_posts(self.request.query_params)

    def perform_create(self, serializer):
        
        user = self.request.user
        if not user or not user.is_authenticated:
            
            if not self.request.data.get("author_id"):
                from rest_framework.exceptions import PermissionDenied
                raise PermissionDenied("Authentication required to create posts or provide valid author_id.")
        serializer.save()

class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.select_related("author").all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
