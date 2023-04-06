
class ChildClassBuilder:
    ...

    def set_type(self, t: Type):
        self.t = t

    def build():
        instance = self.t()
        ...
        return instance
