class Ddefault:

    def __init__(self):
        vars(self).setdefault('default', self.set_default())
        vars(self).setdefault('default', self.set_default())

    def set_default(self):
        print(vars(self))
        return 'default'

if __name__ == "__main__":
    Ddefault()