temp = self.wfile.getvalue()
if temp:
    self.socket.sendto(temp, self.client_address)