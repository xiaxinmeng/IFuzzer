from xmlrpc.server import SimpleXMLRPCServer
from subprocess import Popen, DEVNULL

def notepad_me():
    try:
        cmd = ['c:\\windows\\notepad.exe']
        p = Popen(cmd, stdin=DEVNULL, stdout=DEVNULL, stderr=DEVNULL)
        return True
    except Exception as e:
        return False

class NetServer(SimpleXMLRPCServer):
    def __init__(self, address):
        super(NetServer, self).__init__(address)
        self.register_introspection_functions()
        self.register_function(notepad_me)

with NetServer(("0.0.0.0", 7777)) as server:
    server.serve_forever()