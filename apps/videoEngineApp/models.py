# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.db import models

# Create your models here.

dir_path = os.path.dirname(os.path.realpath(__file__))
new_dir_path = dir_path + "/uploadedVideos"
print(new_dir_path)
class Video(models.Model):
    video = models.FileField(('Video'), upload_to="videoEngineApp/uploadedVideos/")
    video_views = models.IntegerField(default=0)
    upload_date = models.DateTimeField(auto_now_add=True)
    video_description = models.CharField(max_length=860)

class Event(models.Model):
    event_id = models.IntegerField()
    name = models.CharField(max_length = 245)
    address = models.CharField(max_length = 245)
    header_image = models.CharField(max_length = 245)
    start_date = models.CharField(max_length = 245)
    end_date = models.CharField(max_length = 245)
    start_time = models.CharField(max_length = 245)
    long = models.DecimalField(max_digits=8, decimal_places=3)
    lat = models.DecimalField(max_digits=8, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class CurrentEvent(models.Model):
    event_id = models.IntegerField()
    name = models.CharField(max_length = 245)
    address = models.CharField(max_length = 245)
    header_image = models.CharField(max_length = 245)
    start_date = models.CharField(max_length = 245)
    end_date = models.CharField(max_length = 245)
    start_time = models.CharField(max_length = 245)
    long = models.DecimalField(max_digits=8, decimal_places=3)
    lat = models.DecimalField(max_digits=8, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Media(models.Model):
    # Adding features to allow more functionality with the front end
    views = models.IntegerField(default = 0)
    starred = models.IntegerField(default = 0)
    featured = models.IntegerField(default = 0) # whether a user wants to have it on their social feed or not
    user_id = models.IntegerField(default=False)
    device_id = models.IntegerField(default=False)
    # the event_id needs to be able to be manipulated to the id that we want it to be
    # event_id = models.IntegerField(default=getCurrentEventId) # default value is the value that will be passed to all of the incoming api posts for new media
    event_id = models.IntegerField(default=0)
    media_type = models.CharField(max_length=10) # either image, or video 
    link = models.CharField(max_length=245)
    raw_or_edited = models.CharField(max_length=45) # either raw, edited, or curated, profile, or header
    downloaded = models.IntegerField(default=False)
    ranking = models.IntegerField(default=1)
    date = models.CharField(max_length = 245)
    date_time = models.CharField(max_length = 245)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    gif_link = models.CharField(max_length=245)
    # Meta data to go along with every piece fo data for analysis
    media_length = models.DecimalField(max_digits=8, decimal_places=3, default=0.00)
    media_size = models.DecimalField(max_digits=8, decimal_places=3, default=0.00)
    user_rating = models.IntegerField(default=0)
    curator_rating = models.IntegerField(default=0)
    bitrate = models.IntegerField(default=0)
    total_bitrate = models.IntegerField(default=0)


def __str__(self):
        return '%s %s' % (self.link, self.body)