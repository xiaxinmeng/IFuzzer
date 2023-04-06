# Tell the httplib that we want to use our hack.
httplib.HTTPConnection.response_class = FastHTTPResponse