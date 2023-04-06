from typing import ParamSpec
P = ParamSpec("P")
print(P.args == P.args)  # False
print(P.kwargs == P.kwargs)  # False