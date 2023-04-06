import copy
copy._deepcopy_dispatch[types.MethodType] = copy._deepcopy_atomic