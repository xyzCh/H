#!/usr/bin/python


class HttpResponse:
    def __init__(self,connection):
        self.ContentType="text/html"
        self.Charset="utf-8"
        self.__connection=connection
    def Write(self,out):
        http_response = """
HTTP/1.1 200 OK
Cache-Control: private
Content-Type: %s;charset=%s
Server: X-Server/0.001
X-Powered-By: Python 27

"""%(self.ContentType,self.Charset)
        self.__connection.sendall(http_response.encode()+out.encode())

               
    def End(self):
        self.__connection.close()
