def dist_for_module(name, spec):
    where = dirname(dirname(spec.origin))
    dist, = metadata.distributions(name, path=[where])
    return dist