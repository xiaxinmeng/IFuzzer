from dataclasses import dataclass, field


@dataclass
class Foo:
    _bar: int = field(init=False)
    
    @property
    def bar(self):
        return self._bar

    @bar.setter
    def bar(self, value):
        self._bar = value
    
    # field is required,
    # uses descriptor bar for get/set
    bar: int = field(descriptor=bar)