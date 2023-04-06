def _deepcopy_method(x, memo):
    return type(x)(x.im_func, deepcopy(x.im_self, memo), x.im_class)
d[types.MethodType] = _deepcopy_method