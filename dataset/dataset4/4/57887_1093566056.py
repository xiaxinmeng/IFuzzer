def unique(varname, value, scope):
    assert(not varname in scope);
    scope[varname] = value;