
import array
a = array.array('b',  [ord('g')])
a.__deepcopy__('str')
a.__deepcopy__(1)
a.__deepcopy__([1,'str'])
