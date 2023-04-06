
import pickle
from types import MappingProxyType
eggs = MappingProxyType(dict(sausage=True))
pickle.dumps(eggs)
