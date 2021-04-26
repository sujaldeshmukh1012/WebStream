from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from video_stream.models import Video
from .filters import videoSearch
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def home(request):
    allvideo = Video.objects.all()
    videocount = Video.objects.count()

    searchFilter = videoSearch(request.GET, queryset=allvideo)

    allvideo = searchFilter.qs

    context = {
        'allvideo': allvideo,
        'searchFilter': searchFilter,
        'count': videocount
    }
    return render(request, 'home.html', context)
