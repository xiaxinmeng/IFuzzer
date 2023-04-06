def test_bizarre(self):   
    class Bizarre(Flag):
        b = 3
        c = 4
        d = 6
    self.assertEqual(repr(Bizarre(7)), '<Bizarre.d|c|b: 7>')