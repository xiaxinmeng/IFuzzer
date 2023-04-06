with self.assertRaises(TypeError):
    list(difflib.unified_diff(a, b, fna, fnb))