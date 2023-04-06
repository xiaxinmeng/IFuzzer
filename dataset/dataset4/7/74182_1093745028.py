from functools import partial
from pprint import pprint, AUTOWIDTH

pprint = partial(pprint, width=AUTOWIDTH)