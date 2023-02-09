from rest_framework.serializers import ModelSerializer
from main_app.models import Song


class SongCreateSerializer(ModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'


class SongCatalogSerializer(ModelSerializer):

    class Meta:
        model = Song
        fields = ['name', 'serial_number_in_album']

