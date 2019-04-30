from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import sys, os, base64, datetime, hashlib, hmac, pytz, json, urllib, requests
from django.db import models

def Giffing(videoPassed):
	# files = os.listdir(toGifPath)
	# files.sort()
	# for idx, file in enumerate(files):
	# 	clip = VideoFileClip(toGifPath + "/" + file) 
	# 	start = 5.0
	# 	end = 7.0
	# 	if (clip.duration < 5):
	# 		start = 0.0
	# 		end = clip.duration
	# 	clip = (clip.subclip((0,start),(0,end)).resize(0.3))
	# 	clip.write_gif(alreadyGifedPath + "/mediaId_ (%d).gif" % (idx + 50))
    return videoPassed