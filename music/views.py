from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import Track, Playlist
from .serializers import TrackSerializer, PlaylistSerializer

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all().order_by('-created_at')
    serializer_class = TrackSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all().order_by('-created_at')
    serializer_class = PlaylistSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)