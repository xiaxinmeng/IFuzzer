import pickle
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class ExampleDataclass:
    foo: str
    bar: int