print("file name:", __file__)
import traceback
try:
    aaa
except:
    traceback.print_exc()
    raise