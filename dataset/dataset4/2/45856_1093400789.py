import copy
import types

def _deepcopy_method(x, memo):
    return type(x)(x.im_func, deepcopy(x.im_self, memo), x.im_class)
copy._deepcopy_dispatch[types.MethodType] = _deepcopy_method

from scikits.openopt import NLP
p = NLP(lambda x: x**2, 1)
p3 = _deepcopy_method(p, None)