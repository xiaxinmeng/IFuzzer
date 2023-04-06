
class _AttributeHolder(object):
    def __init__(self, sort=false):
        self.sort = sort

    def _get_kwargs(self):
        if sort:
            return sorted(self.__dict__.items())
        else:
            return self.__dict__.items()
