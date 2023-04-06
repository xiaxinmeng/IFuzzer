with self.assertRaises(TypeError):
    ClassVar[int, str]
with self.assertRaises(TypeError):
    Final[int, str]