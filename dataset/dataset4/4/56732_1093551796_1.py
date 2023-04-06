def initiate_send(self):
    while self.producer_fifo and self.connected:
        first = self.producer_fifo[0]
        ...
        try:
            data = buffer(first, 0, obs)
        except TypeError:
            data = first.more() <--- here 