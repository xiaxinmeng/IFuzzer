class Context(object):
    def __init__(self):
        for name, val in locals().items():
            setattr(self, name, val)