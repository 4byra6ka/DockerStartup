from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import IsModerator, IsOwner
from users.serializers import UserSerializer, UserCreateSerializer


class UsersCreateView(generics.CreateAPIView):
    """Контроллер создания пользователя"""
    serializer_class = UserCreateSerializer


class UsersListView(generics.ListAPIView):
    """Контроллер списка пользователей"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsModerator]


class UsersDetailView(generics.RetrieveAPIView):
    """Контроллер описания пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsOwner]
    lookup_field = 'username'


class UsersUpdateView(generics.UpdateAPIView):
    """Контроллер обновления пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsOwner]
    lookup_field = 'username'


class UsersDeleteView(generics.DestroyAPIView):
    """Контроллер удаления пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsOwner]
    lookup_field = 'username'
