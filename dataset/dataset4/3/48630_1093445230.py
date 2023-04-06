from functools import partial
from copy import deepcopy

p = partial("Hello world".replace, "world")
p("mom")
p2 = deepcopy(p)