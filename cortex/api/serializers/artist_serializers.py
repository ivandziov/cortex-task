from rest_framework.serializers import ModelSerializer
from main_app.models import Artist
from .album_serializers import AlbumCatalogSerializer


class ArtistCreateSerializer(ModelSerializer):

    class Meta:
        model = Artist
        fields = '__all__'


class ArtistCatalogListSerializer(ModelSerializer):
    albums = AlbumCatalogSerializer(many=True)

    class Meta:
        model = Artist
        fields = ['name', 'albums']
