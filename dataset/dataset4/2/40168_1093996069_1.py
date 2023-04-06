class Player:
    def __init__(self, name):
        self.xname = name

    def __repr__(self):
        return repr(self.__dict__)