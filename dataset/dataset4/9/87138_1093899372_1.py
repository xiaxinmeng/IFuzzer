class VerboseDel:
    def __del__(self):
        print("DELETE OBJECT")
obj = VerboseDel()