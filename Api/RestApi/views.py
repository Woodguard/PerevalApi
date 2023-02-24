from django.shortcuts import render
from rest_framework import generics
from .permissions import IsAdminOrReadOnly
from RestApi.models import Pereval_add, Pereval_images
from RestApi.serializers import PerevalASerializer, PerevalISerializer, UpdateSerializer


# Create your views here.
class PAAPIList(generics.ListCreateAPIView):
    queryset = Pereval_add.objects.all()
    serializer_class = PerevalASerializer


class PAAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Pereval_add.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = (IsAdminOrReadOnly,)


class PAAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Pereval_add.objects.all()
    serializer_class = PerevalASerializer
    permission_classes = (IsAdminOrReadOnly,)


class PIAPIList(generics.ListCreateAPIView):
    queryset = Pereval_images.objects.all()
    serializer_class = PerevalISerializer


class PIAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Pereval_images.objects.all()
    serializer_class = PerevalISerializer
    permission_classes = (IsAdminOrReadOnly,)
