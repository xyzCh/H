#!/usr/bin/python

class HttpRequest:
    def __init__(self):
        self.Cookie={}
        self.Params={}
        self.Get={}
        self.Post={}
        self.Host=""
        self.Type=""
