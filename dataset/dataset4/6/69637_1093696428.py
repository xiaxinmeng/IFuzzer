def transparency_get(self, x, y):
    """Returns a boolean indicating if the pixel at (x,y) is transparent. """
    
    return self.tk.call(self.name, 'transparency', 'get', x, y)

def transparency_set(self, x, y, boolean=True):
    """Make pixel at (x,y) transparent if boolean is true, opaque otherwise. """
    
    self.tk.call(self.name, 'transparency', 'set', x, y, boolean)