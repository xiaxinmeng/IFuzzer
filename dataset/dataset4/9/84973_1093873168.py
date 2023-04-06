from dataclasses import field, make_dataclass

fieldspec1 = ('field1', str)
fieldspec2 = ('field2', str, field(default='Hello'))

MyDc1 = make_dataclass('MyDc1', [fieldspec1, fieldspec2]) # Ok
MyDc2 = make_dataclass('MyDc2', [fieldspec2, fieldspec1]) # TypeError