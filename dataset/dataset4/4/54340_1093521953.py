import copy, pickle
from xml.dom.minidom import NodeList

obj = NodeList()
obj.append('a')

obj2 = copy.deepcopy(obj)
print(obj2)

obj2 = pickle.loads(pickle.dumps(obj))
print(obj2)