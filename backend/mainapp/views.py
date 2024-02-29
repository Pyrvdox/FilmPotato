from django.shortcuts import render
from rest_framework import generics
from .models import Movie
from .serializers import MovieModelSerializer
from rest_framework.response import Response

# Create your views here.
class MovieAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer

class SingleMovieAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer