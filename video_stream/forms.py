from django import forms
from .models import VideoResponse


class VideoResponseForm(forms.ModelForm):
    response = forms.CharField(
        widget=forms.TextInput(), max_length=500, required=True)

    class Meta:
        model = VideoResponse
        fields = ('response',)
