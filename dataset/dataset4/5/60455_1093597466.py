class Proxy:
    def __init__(self, proxied_object):
        self.proxied_object = proxied_object
        self.id = id(proxied_object)
    def __getattr__(self, name):
        return getattr(self.proxied_object, name)