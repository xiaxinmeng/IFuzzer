from inspect import is_decorator_call

def set_hello_tag(tag='world'):
    if is_decorator_call():
        # called without parenthesis!
        # the decorated object is `tag`
        return set_hello_tag()(tag)   # note that `is_decorator_call` should not return True for this call
    else:
        def decorate(f):
            setattr(f, 'hello', tag)  # set a hello tag on the decorated f
            return f
        return decorate