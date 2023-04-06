class TestHeap(unittest.TestCase):

    def test_nsmallest(self):
        self.assertEqual(heapq.nsmallest(3, range(10)), [0,1,2])
        ...