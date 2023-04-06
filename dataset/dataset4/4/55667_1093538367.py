def get_headers( self, file_name ):
    sock = socket.socket()
    sock.bind(('localhost',0))
    fd = sock.makefile()
    handle = tarfile.open( file_name,'r',fileobj=fd ) # This line breaks