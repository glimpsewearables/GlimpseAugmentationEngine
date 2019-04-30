from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import sys, os, base64, datetime, hashlib, hmac, pytz, json, urllib, requests
from django.db import models
from os import listdir

def VideoEditor(videoPassed):
    print("Video Editing function from VideoEditor.Py with " + videoPassed + " as the video passed")
    return videoPassed