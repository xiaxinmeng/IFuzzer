
class O(B, metaclass=C):
    def _super(self):
        return super()
    def __init_subclass__(cls, /, *args, **kwargs):
        return super().__init_subclass__(*args)
