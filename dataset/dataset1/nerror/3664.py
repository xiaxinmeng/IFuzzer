import _pickle
obj = _pickle.Pickler(open("/bin/ls")) #can be open(__file__) for scripts
try: obj.__init__('pouet', 87)
except Exception as err: pass

obj.dump(0)
