from rest_framework import serializers
from .models import Track, Playlist

class TrackSerializer(serializers.ModelSerializer):
    audio_file = serializers.FileField(required=False, allow_null=True)
    artwork = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Track
        fields = ['id', 'title', 'artist', 'audio_file', 'artwork', 'created_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')

        # AUDIO
        if instance.audio_file:
            try:
                url = instance.audio_file.url
                if request:
                    url = request.build_absolute_uri(url)
                data['audio_file'] = url
            except:
                data['audio_file'] = None
        else:
            data['audio_file'] = None

        # ARTWORK
        if instance.artwork:
            try:
                art = instance.artwork.url
                if request:
                    art = request.build_absolute_uri(art)
                data['artwork'] = art
            except:
                data['artwork'] = None
        else:
            data['artwork'] = None

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