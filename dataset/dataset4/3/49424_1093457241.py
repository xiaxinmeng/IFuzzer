def python_logo():
     handle = open("python_logo.jpg")
     return xmlrpclib.Binary(handle.read())
     handle.close()