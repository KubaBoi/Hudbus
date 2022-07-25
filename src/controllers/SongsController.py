
import os

from Cheese.cheeseController import CheeseController as cc
from Cheese.resourceManager import ResMan

#@controller /songs;
class SongsController(cc):

    #@get /getAll;
    @staticmethod
    def getAll(server, path, auth):
        fls = []
        for root, dirs, files in os.walk(ResMan.web("songs")):  
            for file in files:
                if (file == ".gitkeep"): continue
                fls.append(file)

        return cc.createResponse({"SONGS": fls})
