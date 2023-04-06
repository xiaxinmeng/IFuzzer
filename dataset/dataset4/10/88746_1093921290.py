class MyMap(Mapping):
    def __init__(self, **kwargs) -> None:
        self.data = {
            k:v for k, v in kwargs.items()
        }

    def __getitem__(self, k):
        return self.data.get(k)

    def __len__(self):
        return self.data.__len__()

    def __iter__(self):
        return self.data.__iter__()


info = MyMap(
    foo="bar",
    baz=MyMap(bar="foo")
)

pprint(info)