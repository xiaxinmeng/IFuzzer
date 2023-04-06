def datagram_received(self, data, addr):
    if self.recvfrom:
        self.recvfrom.set_result((data, addr))
        self.recvfrom = None