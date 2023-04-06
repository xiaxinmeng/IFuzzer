def check_type(field):
    self.assertTrue(field is None or isinstance(field, str), repr(field))