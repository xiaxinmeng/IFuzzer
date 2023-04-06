class myint(int):
    def __index__(self):
        return int(self) + 1