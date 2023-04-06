class VerboseObject:
    def __setattr__(self, nm, value):
        print(f"Setting {nm} to {value}")
        super().__setattr__(nm, value)

o = VerboseObject()
o.a = 42