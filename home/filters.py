import django_filters
from video_stream.models import Video


class videoSearch(django_filters.FilterSet):
    class Meta:
        model = Video
        fields = ['title']
