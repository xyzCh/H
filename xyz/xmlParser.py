import xml.dom.minidom

def Parser():
    result={}
    webconf=xml.dom.minidom.parse("web.xml")
    root=webconf.documentElement
    if root.nodeName=="webconf":
        items=root.getElementsByTagName("item")
        for item in items:
            if item.hasAttribute("id"):
                id=item.getAttribute("id");
                val=item.childNodes[0].data
                result[id]=val
    return result
