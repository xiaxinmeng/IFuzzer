class C:
    count = 0
    def __init__(self):
        count = self.__class__.count
        self.__class__.count = count + 1
        setattr(self, f'a{count}', count)