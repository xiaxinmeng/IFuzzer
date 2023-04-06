import dataclasses


@dataclasses.dataclass
class Demo:
  field_a: object

class Obj:
   def __init__(self, x):
    self._x = x

   def __deepcopy__(self, *args):
     raise ValueError('BOOM!')


###
d1 = Demo(field_a=Obj([1,2,3]))
dd = dataclasses.asdict(d1)