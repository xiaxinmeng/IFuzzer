def test_register_kwargs(self):
    name = 'fedcba'
    csv.register_dialect(name, delimiter=';')
    try:
        self.assertTrue(csv.get_dialect(name).delimiter, '\t')
        self.assertTrue(list(csv.reader('X;Y;Z', name)), ['X', 'Y', 'Z'])
    finally:
        csv.unregister_dialect(name)