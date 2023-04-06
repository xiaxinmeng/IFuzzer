
from graphlib import TopologicalSorter
from types import GenericAlias

if not hasattr(TopologicalSorter, "__class_getitem__"):  # pragma: no cover
    TopologicalSorter.__class_getitem__ = classmethod(GenericAlias)  # type: ignore
