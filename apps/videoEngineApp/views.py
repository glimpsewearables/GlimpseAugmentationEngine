# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import sys, os, datetime, json, urllib, requests
from django.db import models
from os import listdir
from .VideoEditing import Giffing, MetaData, VideoIndexing, VideoEditor, VideoStabilizer

desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
cwd = os.getcwd()
filePathDownload = desktop + "/Videos/Downloaded"
filePathUpload = desktop + "/Videos/Edited"
serverFileDownload = cwd + "/uploadedVideos/pre"
serverFileUpload = cwd + "/uploadedVideos/post"
rawFiles = os.listdir(filePathDownload)
editedFiles = os.listdir(filePathUpload)

def index(request):
    return render(request, "index.html")
    # return HttpResponse(filePath)

def uploadFile(request):
    if request.POST:
        editType = request.POST["fileChosen"]
        videoURL = "https://s3-us-west-2.amazonaws.com/users-raw-content/user3_video_2019-04-12_19.17.36.mp4"
        videoName = videoURL.split("https://s3-us-west-2.amazonaws.com/users-raw-content/")
        # urllib.request.urlretrieve(videoURL, serverFileDownload + "/" + videoName[1])
        urllib.request.urlretrieve(videoURL, filePathDownload + "/" + videoName[1])
        if editType == "fileOne":
            scriptOne("image file chosen")
        elif editType == "fileTwo":
            scriptTwo("image file chosen")
        elif editType == "fileThree":
            scriptThree("image file chosen")
        elif editType == "fileFour":
            scriptFour("image file chosen")
        elif editType == "fileFive":
            scriptFive("image file chosen")
    return redirect("/")

def testing(request):
    return HttpResponse("testing")

def scriptOne(filePassed):
    # All Code for editing the file in this function
    # This will be the giffing script
    newFileAfterEdit = "new file after edits"
    scriptOneFromGiffing = Giffing.Giffing("Video Passed to Giffing")

    return newFileAfterEdit

def scriptTwo(filePassed):
    # All Code for editing the file in this function
    # This will be the video indexing script
    newFileAfterEdit = "new file after edits"
    scriptTwoFromVideoIndexing = VideoIndexing.VideoIndexing("Video passed to Video Indexer")
    return newFileAfterEdit

def scriptThree(filePassed):
    # All Code for editing the file in this function
    # This will be the video editing script, changing exposure, saturation, etc
    newFileAfterEdit = "new file after edits"
    scriptThreeFromVideoEditing = VideoEditor.VideoEditor("Video Passed to video editor")
    return newFileAfterEdit

def scriptFour(filePassed):
    # All Code for editing the file metadata in this function
    # This will be 
    newFileAfterEdit = "new file after edits"
    scriptFourFromMetaData = MetaData.MetaData("Video Passed to video editor")
    return newFileAfterEdit

def scriptFive(filePassed):
    # All Code for editing the file in this function
    newFileAfterEdit = "new file after edits"
    scriptFiveFromVideoStabilizer = VideoStabilizer.VideoStabilizer("Video Passed to video editor")
    return newFileAfterEdit


