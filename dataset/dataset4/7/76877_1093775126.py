import pickle
class CustomException(Exception):
    def __init__(self, arg1, arg2):
        msg = "Custom message {} {}".format(arg1, arg2)
        super().__init__(msg)


obj_dump = pickle.dumps(CustomException("arg1", "arg2"))
obj = pickle.loads(obj_dump)