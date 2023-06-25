from rest_framework import generics, viewsets, views
from .serializers import GenreSerializer, ArtistSerializer, AlbumSerializer, SongSerializer, PlaylistSerializer
from base.models import Genre, Artist, Album, Song, Playlist
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class GenresList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminUser]


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminUser]


class ArtistVS(viewsets.ViewSet):
    queryset = Artist.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = ArtistSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        artist = get_object_or_404(self.queryset, pk=pk)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)

    def update(self, request, pk=None):
        artist = get_object_or_404(self.queryset, pk=pk)
        serializer = ArtistSerializer(artist, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        artist = get_object_or_404(self.queryset, pk=pk)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlbumModelVS(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]


class SongsList(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]


class PlaylistView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Playlist.objects.all()
        serializer = PlaylistSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class PlaylistDetail(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            playlist = Playlist.objects.get(id=pk)

        except Playlist.DoesNotExist:
            return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PlaylistSerializer(playlist)
        return Response(serializer.data)

    def put(self, request, pk):
        playlist = Playlist.objects.get(id=pk)
        serializer = PlaylistSerializer(playlist, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        playlist = Playlist.objects.get(id=pk)
        playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
