class Proxy(object):
    def __init__(self, proxied):
        self.proxied = proxied
    @property
    def __class__(self):
        return self.proxied.__class__
    def __call__(self):
        return self.proxied.__call__()

p = Proxy(lambda: 1)
p.__class__.__call__(p)