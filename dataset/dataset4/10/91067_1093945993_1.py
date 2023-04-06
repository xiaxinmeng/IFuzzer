parentdir = max(filter(__file__.startswith, sys.path), key=len)
sys.path.remove(parentdir)
del sys.modules['encodings']
import encodings