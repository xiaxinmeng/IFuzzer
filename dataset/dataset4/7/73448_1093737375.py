sig = inspect.signature(f)
ann = sig.parameters['arg1'].annotation
is_an_union = isinstance(ann, typing._Union)