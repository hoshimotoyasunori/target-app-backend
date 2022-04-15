from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .serializers import UserSerializer,LargeSerializer ,MiddleSerializer ,TaskSerializer
from .models import Large, Middle, Task



class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class LargeListView(generics.ListAPIView):
    queryset = Large.objects.all()
    serializer_class = LargeSerializer
    permission_classes = (AllowAny,)

class LargeRetrieveView(generics.RetrieveAPIView):
    queryset = Large.objects.all()
    serializer_class = LargeSerializer
    permission_classes = (AllowAny,)

class LargeViewSet(viewsets.ModelViewSet):
    queryset = Large.objects.all()
    serializer_class = LargeSerializer


class MiddleListView(generics.ListAPIView):
    queryset = Middle.objects.all()
    serializer_class = MiddleSerializer
    permission_classes = (AllowAny,)

class MiddleRetrieveView(generics.RetrieveAPIView):
    queryset = Middle.objects.all()
    serializer_class = MiddleSerializer
    permission_classes = (AllowAny,)

class MiddleViewSet(viewsets.ModelViewSet):
    queryset = Middle.objects.all()
    serializer_class = MiddleSerializer


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)

class TaskRetrieveView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

