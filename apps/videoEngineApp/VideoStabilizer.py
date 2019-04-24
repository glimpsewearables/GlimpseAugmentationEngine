from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import sys, os, base64, datetime, hashlib, hmac, pytz, json, urllib, requests
from django.db import models

def VideoStabilizer(videoPassed):
    print("Video Stabilization function from VideoStabilier.py with " + videoPassed + " as the video passed")
    return videoPassed