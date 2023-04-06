convert = {
  '__lt__': [
    ('__gt__',
      lambda self, other: not_op_and_not_eq(self.__lt__, self, other)),
    ('__le__',
      lambda self, other: op_or_eq(self.__lt__, self, other)),
    ('__ge__',
      lambda self, other: not_op(self.__lt__, other))
  ],
  '__le__': [
    ('__ge__',
      lambda self, other: not_op_or_eq(self.__le__, self, other)),
    ('__lt__',
      lambda self, other: op_and_not_eq(self.__le__, self, other)),
    ('__gt__',
      lambda self, other: not_op(self.__le__, other))
  ],
  '__gt__': [
    ('__lt__',
      lambda self, other: not_op_and_not_eq(self.__gt__, self, other)),
    ('__ge__',
      lambda self, other: op_or_eq(self.__gt__, self, other)),
    ('__le__',
      lambda self, other: not_op(self.__gt__, other))
  ],
  '__ge__': [
    ('__le__',
      lambda self, other: not_op_or_eq(self.__ge__, self, other)),
    ('__gt__',
      lambda self, other: op_and_not_eq(self.__ge__, self, other)),
    ('__lt__',
      lambda self, other: not_op(self.__ge__, other))
  ]
}