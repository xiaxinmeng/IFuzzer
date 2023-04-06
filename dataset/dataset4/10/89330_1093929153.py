
from copy import deepcopy


class X(dict):
    def __deepcopy__(self, memo):
        return self


print(deepcopy(X()))
print(deepcopy(X))

print(type(X[str, int]))
print(deepcopy(X[str, int]()))
print(deepcopy(X[str, int]))
