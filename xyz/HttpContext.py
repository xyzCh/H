#time:2017-6-6
#author:xyz
#!/usr/bin/python

import HttpRequest
import HttpResponse

class HttpContext:
    def __init__(self,connection):
        self.Request=HttpRequest.HttpRequest()
        self.Response=HttpResponse.HttpResponse(connection)
    

