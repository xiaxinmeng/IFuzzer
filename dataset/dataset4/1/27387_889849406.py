ns = {}

exec("""
import typing

__name__ = None

T = typing.TypeVar("T")
P = typing.ParamSpec("P")
NT = typing.NewType("NT", int)
""", ns)

for o in (ns["T"], ns["P"], ns["NT"]):
    print(o, o.__module__)