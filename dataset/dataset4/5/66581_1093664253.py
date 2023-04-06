class NTF(NamedTemporaryFile):
    def __init__(self, *args, closed=False, **kwargs):
        if closed: kwargs["delete"] = True
        super().__init__(*args, **kwargs)
        if closed: self.close()