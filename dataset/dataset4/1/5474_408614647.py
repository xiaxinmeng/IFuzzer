namespace = {
    '__name__': mod_spec.name, # This should then be replaced to just '__main__' to run it, right?
    '__file__': mod_spec.origin,  # This won't work for things like builtins or any other *non-locatable*
    '__package__': mod_spec.parent,
    '__loader__': mod_spec.loader,
    '__spec__': mod_spec,
    '__cached__': None,
}   