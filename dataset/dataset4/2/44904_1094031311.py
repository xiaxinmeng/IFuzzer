class C:
    # There's no @classmethod decorator here as there should have been
    def __instancecheck__(self, arg):
        return False

isinstance(42, C)