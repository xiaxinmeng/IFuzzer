from struct import Struct
import copy, copyreg
def pickle_struct(s):
    return Struct, (s.format,)

copyreg.pickle(Struct, pickle_struct)

s1 = Struct('<i')
s2 = copy.deepcopy(s1)