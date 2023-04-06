class Segfault:
    def __getattr__(self, name):
        self.unknown_attribute

instance = Segfault()
issubclass(instance, int)  # int doesn't matter