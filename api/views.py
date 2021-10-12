from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets

from .serializers import TrainingSerializer, ContentSerializer, UserSerializer
from .models import Training, Content


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class TrainingListView(generics.ListAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    permission_classes = (AllowAny,)


class TrainingRetrieveView(generics.RetrieveAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    permission_classes = (AllowAny,)


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class ContentListView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = (AllowAny,)


class ContentRetrieveView(generics.RetrieveAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = (AllowAny,)


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
