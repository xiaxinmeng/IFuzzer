class Obj:
    def __del__(self):
        raise Exception("broken del")

    def __repr__(self):
        raise Excepiton("broken repr")

obj = Obj()
del obj