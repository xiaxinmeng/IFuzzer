def f(a, b, context=None):
    with localcontext(context):
        return a / b