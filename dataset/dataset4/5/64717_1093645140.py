from PyQt4.QtCore import QObject, QTimer
# QObject is the parent of QTimer

class A(QObject):
    pass

class B(A, QTimer):
    pass

class C(QTimer, A):
    pass

print(B.__base__, B.__mro__)
print(C.__base__, C.__mro__)