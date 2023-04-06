class VerboseDel:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print(self.name)

a = VerboseDel("a")
b = VerboseDel("b")
c = VerboseDel("c")