from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User

from users.serializers import UserSerializer, ProfileViewSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        security=[{"Bearer": []}],
        responses={200: 'Успешный запрос', 403: 'Forbidden'}
    )
    def get(self, request):
        """Get user's profile."""
        user = request.user
        # Получаем информацию о пользователе
        serializer = ProfileViewSerializer(user)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)
