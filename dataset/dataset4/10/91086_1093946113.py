class ExampleCls:
    @classmethod
    def iter_cls(cls):
        for name, val in cls.__dict__.items():
            print(cls.__annotations__)