#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Cheese.cheeseController import CheeseController as cc

#@controller /android;
class AndroidController(cc):

    #@get /web;
    @staticmethod
    def web(server, path, auth):
        return cc.createResponse()
