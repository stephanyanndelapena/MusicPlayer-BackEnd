from django.conf import settings
from urllib.parse import urlparse
from rest_framework import serializers
from .models import Track, Playlist


class FlexibleImageField(serializers.ImageField):
    
    def to_internal_value(self, data):
        
        if isinstance(data, str):
            return data
        return super().to_internal_value(data)


class TrackSerializer(serializers.ModelSerializer):
    audio_file = serializers.FileField(required=False, allow_null=True)
    artwork = FlexibleImageField(required=False, allow_null=True, use_url=True)

    class Meta:
        model = Track
        fields = ['id', 'title', 'artist', 'audio_file', 'artwork', 'created_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')

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

    def update(self, instance, validated_data):
        artwork_value = validated_data.pop('artwork', serializers.empty)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if artwork_value is not serializers.empty:
            if artwork_value is None:
                instance.artwork = None
            elif isinstance(artwork_value, str):
                try:
                    media_url = settings.MEDIA_URL or '/media/'
                    if media_url and media_url in artwork_value:
                        rel = artwork_value.split(media_url, 1)[1]
                    else:
                        parsed = urlparse(artwork_value)
                        path = parsed.path or artwork_value
                        if '/media/' in path:
                            rel = path.split('/media/', 1)[1]
                        else:
                            rel = path.lstrip('/')
                    instance.artwork.name = rel
                except Exception:
                    
                    pass
            else:
                
                instance.artwork = artwork_value

        instance.save()
        return instance


class PlaylistSerializer(serializers.ModelSerializer):
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