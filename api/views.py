from rest_framework import viewsets, filters
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Post, Comment, Group, Follow, User
from .serializers import PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer


class OwnResourcePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ("DELETE", "PUT", "POST", "PATCH"):
            return request.user == obj.author
        return True


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=group__id']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__username', '=following__username']

    def perform_create(self, serializer):
        # following = get_object_or_404(User, username=self.request.data.get("following"))

        serializer.save(user=self.request.user)
