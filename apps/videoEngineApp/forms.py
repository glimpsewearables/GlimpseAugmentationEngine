from django import forms

class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["video_description", "videofile"]