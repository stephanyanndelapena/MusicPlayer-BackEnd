from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from .models import Track, Playlist
from .serializers import TrackSerializer, PlaylistSerializer
import logging

logger = logging.getLogger(__name__)


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all().order_by('-created_at')
    serializer_class = TrackSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def partial_update(self, request, *args, **kwargs):
       
        instance = self.get_object()
        logger.debug('partial_update called for Track id=%s', getattr(instance, 'id', None))
        logger.debug('Incoming request.data keys: %s', list(request.data.keys()))
        logger.debug('Incoming request.data preview: %s', {k: (type(v).__name__ if k == 'artwork' else str(v)[:200]) for k, v in request.data.items()})

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if not serializer.is_valid():
            logger.warning('Track partial_update validation errors: %s', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all().order_by('-created_at')
    serializer_class = PlaylistSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)