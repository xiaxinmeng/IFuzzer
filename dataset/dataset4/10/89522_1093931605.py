
from graphlib import TopologicalSorter
x: 'TopologicalSorter[str]' = TopologicalSorter({"a": {}, "b": {"a"}})
