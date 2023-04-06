class MyList:
    def __getitem__(self, index):
        return index + 1
    def __class_getitem__(cls, item):
        return f"{cls.__name__}[{item.__name__}]"