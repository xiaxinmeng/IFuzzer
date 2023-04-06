def submit_new_urls(uid, l):
    fn = os.path.join(destdir, "%s.newurls" % (uid))
    fd = open("%s.tmp" % fn, "w")
    fd.write("\n".join(l))
    fd.close()
    return "Ok"

server = SimpleXMLRPCServer(("example.com", 8000))
server.socket.setsockopt(socket.SOL_SOCKET, 
socket.SO_REUSEADDR, 0)
server.register_function(submit_new_urls)
server.serve_forever()    