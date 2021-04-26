from django.contrib import admin
from django.http import response
from .models import Video
from .models import VideoResponse

# Register your models here.


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'poster', 'slug', 'video')
    list_filter = ('title', 'slug', 'id')
    search_fields = ('id', 'title', 'slug', 'video')
    ordering = ('-id',)


class VideoResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'forVideo', 'response', 'responded')
    list_filter = ('user', 'forVideo', 'responded')
    search_fields = ('user', 'forVideo', 'responded')
    ordering = ('-responded',)


admin.site.register(Video, VideoAdmin)
admin.site.register(VideoResponse, VideoResponseAdmin)
