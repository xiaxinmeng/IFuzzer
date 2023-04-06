class Obj:

    def __del__():  # sic!
        pass

def run():
    for _ in range(202):
        obj = Obj()

run()