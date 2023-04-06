class TestPickleableException(unittest.TestCase):
    def test_ParseError(self):
        err = ParseError('msg', 2, None, (1, 'context'))
        err2 = pickle.loads(pickle.dumps(err))
        self.assertEqual(vars(err), vars(err2))