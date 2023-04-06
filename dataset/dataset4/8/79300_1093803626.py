class VerboseObject:
    def __setattr__(self, nm, value):
        print(f"Setting {nm} to {value}")
        setattr(self, nm, value)

o = VerboseObject()
o.a = 42