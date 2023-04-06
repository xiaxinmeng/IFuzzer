class Obj:
    def __del__(self):
        raise Exception("broken del")

    def __repr__(self):
        return "<useful repr>"

obj = Obj()
del obj