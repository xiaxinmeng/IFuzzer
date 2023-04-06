class Nasty(str):
    def __del__(self):
        del e.message

e = ValueError(Nasty("msg"))
e.args = ()
del e.message
del e