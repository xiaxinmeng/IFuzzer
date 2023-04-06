from collections import namedtuple
from operator import attrgetter
from pprint import pprint

def namedattrgetter (attr, *attrs):
    ag = attrgetter (attr, *attrs)
    if attrs:
        nt = namedtuple ('_', (attr,) + attrs, rename=True)
        return lambda obj: nt._make (ag (obj))
    else:
        return ag

Person = namedtuple('Person', ['fname', 'lname', 'age', 'email'])
FullName = namedtuple('FullName', ['lname', 'fname'])

people = [
	Person('tom', 'smith', 50, 'tsmith@example.com'),
	Person('sue', 'henry', 40, 'shenry@example.com'),
	Person('hank', 'jones', 30, 'hjones@example.com'),
	Person('meg', 'davis', 20, 'mdavis@example.com'),
]