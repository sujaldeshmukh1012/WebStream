from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, response
from .models import Video, VideoResponse
from .forms import VideoResponseForm
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def stream(request, id_video):
    user = request.user
    video = Video.objects.get(id=id_video)
    strvideo = Video.objects.get(id=id_video)
    if request.method == 'POST':
        form = VideoResponseForm(request.POST, request.FILES)
        if form.is_valid():
            response = form.cleaned_data.get('response')
            p, created = VideoResponse.objects.get_or_create(
                response=response, user=user, forVideo=strvideo)
            p.save()

    else:
        form = VideoResponseForm()

    return render(request, 'index.html', {'video': video, 'form': form})
