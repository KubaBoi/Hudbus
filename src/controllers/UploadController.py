
import os
import requests
import shutil

from pytube import YouTube
from moviepy.editor import *
import eyed3
from eyed3.id3.frames import ImageFrame

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

        videoArgs = cc.getArgs(args["URL"])
        thumbNail = f"https://img.youtube.com/vi/{videoArgs['v']}/0.jpg"
        thumbName = "temp.jpg"

        req = requests.get(thumbNail, stream=True)
        if req.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            req.raw.decode_content = True
            
            # Open a local file with wb ( write binary ) permission.
            with open(thumbName, 'wb') as f:
                shutil.copyfileobj(req.raw, f)
                
            print('Image sucessfully Downloaded: ',thumbName)
        else:
            print('Image Couldn\'t be retreived')

        audiofile = eyed3.load(ResMan.web("songs", mp3Name))
        if (audiofile.tag == None):
            audiofile.initTag()

        audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(thumbName, "rb").read(), "image/jpeg")
        audiofile.tag.images.set(ImageFrame.ARTIST, open(thumbName, "rb").read(), "image/jpeg")
        audiofile.tag.images.set(ImageFrame.ICON, open(thumbName, "rb").read(), "image/jpeg")
        audiofile.tag.images.set(ImageFrame.ILLUSTRATION, open(thumbName, "rb").read(), "image/jpeg")

        audiofile.tag.save()

        os.remove(thumbName)

        return cc.createResponse({"STATUS": "OK"})
