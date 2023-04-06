
from typing import MutableSequence, TypeVar

CliffordGate = TypeVar('CliffordGate')

class QCircuit(MutableSequence[CliffordGate]):
    def __init__(self, gates):
        self.gates = list(gates)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.gates})'
   
    def __getitem__(self, key):
        return self.gates[key]

    def __setitem__(self, key, item):
        self.gates[key] = item

    def __delitem__(self, key):
        del self.gates[key]

    def insert(self, key, item):
        self.gates.insert(key, item)

a = QCircuit(['H0', 'S2'])
a += a
