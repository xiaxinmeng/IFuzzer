__superprivate = "mahog"

class AClass(object):
    def __init__(self, value):
        global __superprivate
        __superprivate = value

    @staticmethod
    def get_sp():
        return __superprivate

if __name__ == "__main__":
    print(__superprivate)  # mahog
    try:
        print(AClass.get_sp()) 
    except NameError as e:
        print(e)           # NameError: name '_AClass__superprivate' is not defined'
    cl = AClass("bla")
    print(cl.get_sp())     # bla
    __superprivate = 1
    print(cl.get_sp())     # bla
    print(AClass.get_sp()) # bla