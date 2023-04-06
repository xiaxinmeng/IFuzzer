
class A:
    def __enter__(self):
        return self
    def __exit__(self, *args, **kwargs):
        raise Exception("Frame is -1 if program is run from command line")

with A():
    raise Exception("Normal Error")
