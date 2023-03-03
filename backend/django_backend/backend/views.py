from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied

from .models import *
from .serializers import *

class FilmListView(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = CreateFilmSerializer

class FilmListIdView(generics.RetrieveUpdateAPIView):
    queryset = Film.objects.all()
    serializer_class = CreateFilmIdSerializer


class AuthoringRetrieveView(generics.RetrieveAPIView):
    queryset = Authoring.objects.all()
    serializer_class = AuthoringSerializer


class AuthoringUpdateView(generics.UpdateAPIView):
    queryset = Authoring.objects.all()
    serializer_class = CreateAuthoringSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class AuthoringCreateView(generics.CreateAPIView):
    queryset = Authoring.objects.all()
    serializer_class = CreateAuthoringSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class AuthoringListView(generics.ListAPIView):
    queryset = Authoring.objects.all()
    serializer_class = AuthoringSerializer