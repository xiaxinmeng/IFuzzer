class Ddefault:

    def __init__(self):
        vars(self).setdefault('default', self.set_default() if not 'default' in vars(self) else self.default)
        vars(self).setdefault('default', self.set_default() if not 'default' in vars(self) else self.default)
        print(vars(self))

    def set_default(self):
        print(vars(self))
        return 'default'

if __name__ == "__main__":
    Ddefault()