from astroid import parse

mod = parse('''from typing import NamedTuple; NamedTuple("A")''')
print(str(next(mod.body[-1].value.infer())))
assert str(next(mod.body[-1].value.infer())) != 'Uninferable'