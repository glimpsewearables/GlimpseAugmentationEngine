from django.conf.urls import url, include
from . import views    # This line is new!

from .resources import VideoResource

video_resource = VideoResource()

urlpatterns = [
    url(r'^$', views.index),
    url(r'^api/', include(video_resource.urls)),
    url(r'^testing', views.testing),
    url(r'^uploadFile', views.uploadFile),
]  