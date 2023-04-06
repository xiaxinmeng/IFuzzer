from struct import Struct
import copy
this_fails = Struct('<i')
copy.deepcopy(this_fails)