def get_entity(name):  # should be a standalone utility function
    try:
        ob = __main__.__dict__[name]
    except KeyError:
        try:
            ob = sys.modules[name]
        except KeyError:
           raise NameError('cannot find %s' % name) from None
    return ob