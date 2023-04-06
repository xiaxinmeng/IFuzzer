def sparse_inner_prod(v1, v2):
    return sum(v1[x]*v2[x] for x in v1.keys() & v2.keys())