class C:
    def __del__(self):
        print('deleted')

c = C()
import pdb; pdb.set_trace()
x = 1