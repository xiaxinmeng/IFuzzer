class Filename:
    def __init__(self, orig):
        self.as_bytes = orig
        self.as_str = myformat(orig)
    def __str__(self):
        return self.as_str
    def __bytes__(self):
        return self.as_bytes