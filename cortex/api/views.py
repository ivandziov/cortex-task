from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from .serializers import ArtistCatalogListSerializer
from .serializers import ArtistCreateSerializer
from .serializers import SongCreateSerializer
from .serializers import AlbumCreateSerializer
from main_app.models import Artist
from main_app.models import Song
from main_app.models import Album


class ArtistCatalogView(ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistCatalogListSerializer


class ArtistCreateView(CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistCreateSerializer


class SongCreateView(CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongCreateSerializer


class AlbumCreateView(CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumCreateSerializer
