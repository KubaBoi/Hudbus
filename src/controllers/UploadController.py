
import os
from pytube import YouTube
from moviepy.editor import *

from Cheese.cheeseController import CheeseController as cc
from Cheese.resourceManager import ResMan

#@controller /upload;
class UploadController(cc):

    #@post /youtube;
    @staticmethod
    def youtube(server, path, auth):
        args = cc.readArgs(server)
        cc.checkJson(["URL"], args)

        ytVideo = YouTube(args["URL"]).streams.filter(progressive=True).last()
        filename = ytVideo.download()
        video = VideoFileClip(filename)
        mp3Name = ".".join(ResMan.getFileName(filename).split(".")[:-1]) + ".mp3"
        video.audio.write_audiofile(ResMan.web("songs", mp3Name))
        video.close()
        os.remove(filename)

        return cc.createResponse({"STATUS": "OK"})
