class SocketSendall(socket.socket):
  _raw_sent = b''
  def sendall(self, data):
    self._raw_sent += data

class TelnetSockSendall(telnetlib.Telnet):
  def open(self, *args, **opts):
    ''' a near-exact copy of Telnet.open '''
    # copy 5 lines from Telnet.open here
    self.sock = SocketSendall(*args, **opts)