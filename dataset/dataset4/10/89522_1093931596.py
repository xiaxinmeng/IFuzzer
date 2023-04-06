
from graphlib import TopologicalSorter

TopologicalSorter[str]({"a": {}, "b": {"a"}})
