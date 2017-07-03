#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys
import xmlParser
from HttpContext import *
from HeaderParser import *

class implRouter:
    def __init__(self,headerStr,_connection):
        self.context=HttpContext(_connection)
        self.conf=xmlParser.Parser()
        self.header=HeaderParser().Parser(headerStr)
        self.connection=_connection
    def __execPy(self):
        webroot=self.conf["webroot"]
        filePath=self.header.filePath
        if os.path.isfile(webroot+filePath):
            f=open(webroot+filePath,"rb")
            try:
                className=f.readline().rstrip().decode().split("@__class:")[1] #获取py处理模块中的类
            except:
                print("Building Class Error:in py file:"+self.header.fileName)
                return
        sys.path.append(webroot+self.header.currRoot)    #加入py处理模块的路径
        module=__import__(self.header.fileName)      #导入py模块
        Handler=getattr(module,className)()     #加载类
        Handler.doRequest(self.context)

    #通用处理
    def __execF(self):
        filePath=self.header.filePath
        webroot=self.conf["webroot"]
        defaultPage=self.conf["defaultPage"]
        if filePath!="/" and filePath.find(".")!=-1:
            if os.path.isfile(webroot+filePath):
                f=open(webroot+filePath,"rb")
                self.context.Response.Write(f.read().decode())
        elif filePath=="/":     #主页
            if os.path.isfile(webroot+"/"+defaultPage):
                f=open(webroot+"/"+defaultPage,"rb")
                self.context.Response.Write(f.read().decode())
        else:
            print("Not Found!")
            ##return 404error
        self.context.Response.End()
    def Exec(self):
        self.context.Request.Get=self.header.Get
        self.context.Request.Post=self.header.Post
        self.context.Request.Cookie=self.header.Cookie
        self.context.Request.Params.update(self.header.Get)
        if self.header.fileType=="py":
            self.__execPy()
        else:
            self.__execF()


    
