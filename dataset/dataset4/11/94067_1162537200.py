def init(self, b=6, id=Test.id):
    self.b = b
    self.__post_init__(id)