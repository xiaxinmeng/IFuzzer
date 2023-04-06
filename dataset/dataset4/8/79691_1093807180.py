
import pickle as pk
import dataclasses as dc

@dc.dataclass
class A:
     pass
pk.dumps(A)  # --> this is fine

B = dc.make_dataclass('B', [], bases=(A,))
pk.dumps(B)  # --> results in an error

# PicklingError: Can't pickle <class 'types.B'>: attribute lookup B on types failed
