from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import sys, os, base64, datetime, hashlib, hmac, pytz, json, urllib, requests
from django.db import models
from os import listdir

def VideoIndexing(videoPassed):
    print("Giffing function from VideoIndexing.py with " + videoPassed + " as the video passed")
    return videoPassed