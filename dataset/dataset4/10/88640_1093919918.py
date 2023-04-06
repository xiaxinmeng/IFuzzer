import inspect


def foo(param, lambda_ref):
    _ = param
    print(str(inspect.getsourcelines(lambda_ref)))


foo(param=0,
    lambda_ref=lambda:
    40 + 2)