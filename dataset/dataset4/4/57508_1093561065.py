class dict2named(dict):
    def __init__(self, *args, **kwargs):
        super(dict2named, self).__init__(*args, **kwargs)
        self.__dict__ = self