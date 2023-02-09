from rest_framework.serializers import ModelSerializer
from main_app.models import Album
from .song_serializers import SongCatalogSerializer


class AlbumCreateSerializer(ModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'


class AlbumCatalogSerializer(ModelSerializer):
    songs = SongCatalogSerializer(many=True)

    class Meta:
        model = Album
        fields = ['name', 'release_year', 'songs']