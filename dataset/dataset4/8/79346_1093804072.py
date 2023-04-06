class MyGetattrClass:
    def __init__(self):
        super().__setattr__("attrs", {})

    def __setattr__(self, name, value):
        self.attrs[name] = value

    def __getattr__(self, name):
        try:
            print(f"{name} equals {self.attrs[name]}")
        except KeyError:
            raise AttributeError(
                f"{type(self).__name__!r} object has no attribute {name!r}"
            ) from None