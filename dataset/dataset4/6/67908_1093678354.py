class Device(object):        
    destroyed = False

    def __del__(self):
        self.destroyed = True

    def _dealloc_vector(self, v):
        if not self.destroyed:
            ...


class Vector(object):        
    def __init__(self, device):
        self.device = device
        
    def __del__(self):
        self.device._dealloc_vector(self)