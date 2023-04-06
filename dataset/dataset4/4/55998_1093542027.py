class InterfaceBase(type):
    ...

Interface = InterfaceBase('Interface', (), {})

class IFoo(Interface):
    ...