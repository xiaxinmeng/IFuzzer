class asyncore_accepting_mixin:
    def __init__(self, sock=None, map=None):
        if map is not None:
            self.map = map
        asyncore.dispatcher.__init__(self, sock, map)
        self.connected = 0
        self.accepting = 1