def test_cannot_subclass_vars(self):
    with self.assertRaises(TypeError):
        class V(TypeVar('T')):
            pass