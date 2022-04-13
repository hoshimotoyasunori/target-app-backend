from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .serializers import UserSerializer,TargetSerializer
from .models import Target


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class TargetListView(generics.ListAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    permission_classes = (AllowAny,)

class TargetRetrieveView(generics.RetrieveAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    permission_classes = (AllowAny,)

class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer

