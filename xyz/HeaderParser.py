#!/usr/bin/python
# -*- coding: utf-8 -*-


class HeaderParser:
    def __init__(self):
        self.Cookie={}
        self.Get={}
        self.Post={}
        self.httpType=""
        self.httpVersion=""
        self.Host=""
        self.currRoot=""    #请求根路径(相对）
        self.filePath=""    #完整的请求路径
        self.fileName=""    #请求文件名
        self.fileType=""    #请求文件类型
    #######################
    def __parser_params(self,arg,url):
        params=url.split("&")
        for p in params:
            p=p.split("=")
            if len(p)==2:
                arg[p[0]]=p[1]
            elif p[-1]=="=":
                arg[p[0]]=""
            else:
                arg[p[0]]=None

    def __parser_filePath(self,url):
        self.filePath=url
        if(url!="/" and url.find(".")!=-1):
            p,d=url.rindex("/"),url.rindex(".")
            self.fileType=url[d+1:]
            self.currRoot=url[0:p+1]
            self.fileName=url[p+1:d]
        else:
            pass
    ########################################
    def Parser(self,str):
        HeaderLines=str.split("\n")
        line=HeaderLines[0].split(" ")
        self.Host=HeaderLines[1].split(" ")[1]
        self.httpType=line[0]
        self.httpVersion=line[2]
        url=line[1].split("?")
        if len(url)>1:
            self.__parser_params(self.Get,url[1])
        else:
            pass       #Post请求
        self.__parser_filePath(url[0])
        #Cookie
        return self
