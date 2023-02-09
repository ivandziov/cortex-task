from django.db.models import Model
from django.db.models import CharField
from django.db.models import ForeignKey
from django.db.models import CASCADE
from django.db.models import PositiveSmallIntegerField


class Artist(Model):
    name = CharField(max_length=100, blank=False, null=False)


class Album(Model):
    name = CharField(max_length=100, blank=False, null=False)
    artist = ForeignKey('Artist', on_delete=CASCADE, blank=False, null=False, related_name='albums')
    release_year = PositiveSmallIntegerField(blank=False, null=False)


class Song(Model):
    name = CharField(max_length=100, blank=False, null=False)
    serial_number_in_album = PositiveSmallIntegerField(blank=False, null=False)
    album = ForeignKey('Album', on_delete=CASCADE, blank=False, null=False, related_name='songs')
