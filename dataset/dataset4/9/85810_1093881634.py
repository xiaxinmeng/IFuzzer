class Foo:
    def __init_subclass__(cls, **kwargs):
        print(kwargs)
Bar = type("Bar", (Foo,), {}, bar=None) # mypy and Pycharm complain
#> {'bar': None}