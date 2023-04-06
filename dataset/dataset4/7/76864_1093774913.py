class Side:

    class Effect(Exception):
        pass

    def __getattribute__(self, name):
        raise Side.Effect()