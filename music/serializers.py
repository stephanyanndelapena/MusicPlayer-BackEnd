from rest_framework import serializers
from .models import Track, Playlist

class TrackSerializer(serializers.ModelSerializer):
    # Make audio_file writable (FileField) so uploads are accepted.
    audio_file = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = Track
        fields = ['id', 'title', 'artist', 'audio_file', 'created_at']

    def to_representation(self, instance):
        """
        Return the same representation as the default serializer but
        replace the audio_file output with an absolute URL (or empty string).
        """
        data = super().to_representation(instance)
        request = self.context.get('request')
        if instance.audio_file:
            try:
                url = instance.audio_file.url
            except ValueError:
                url = ''
            if url and request:
                url = request.build_absolute_uri(url)
            data['audio_file'] = url or ''
        else:
            data['audio_file'] = ''
        return data

class PlaylistSerializer(serializers.ModelSerializer):
    # ensure nested tracks use same context so the audio_file url is absolute
    tracks = serializers.SerializerMethodField()
    track_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Track.objects.all(), source='tracks', required=False
    )

    class Meta:
        model = Playlist
        fields = ['id', 'name', 'description', 'tracks', 'track_ids', 'created_at']

    def get_tracks(self, obj):
        qs = obj.tracks.all()
        return TrackSerializer(qs, many=True, context=self.context).data