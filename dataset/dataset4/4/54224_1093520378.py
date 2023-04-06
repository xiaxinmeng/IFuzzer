import unittest
from threading import Thread
from multiprocessing.pool import ThreadPool


def f(x):
    return x*x


def create_and_run(cb, pool = None):
    if not pool:
        pool = ThreadPool(2)
    r = pool.map_async(f, range(10))
    cb(r.get())


class TestThreadPool(unittest.TestCase):
    def setUp(self):
        self.expected = [f(x) for x in range(10)]

    def callback(self, data):
        self.data = data

    def test_creating_pool_in_mainthread(self):
        """Test multiprocessing.pool.ThreadPool from main thread"""
        self.data = None
        create_and_run(self.callback)
        self.assertEqual(self.data, self.expected)

    def test_creating_pool_in_subthread(self):
        """Test multiprocessing.pool.ThreadPool from a child thread."""
        self.data = None
        t = Thread(target=create_and_run, args=[self.callback])
        t.start()
        t.join()
        self.assertEqual(self.data, self.expected)

    def test_creating_pool_in_subthread_workaround(self):
        """Test running a ThreadPool created in main thread, used in child."""
        self.data = None
        pool = ThreadPool(2)
        t = Thread(target=create_and_run, args=[self.callback, pool])
        t.start()
        t.join()
        self.assertEqual(self.data, self.expected)


if __name__ =='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestThreadPool)
    unittest.TextTestRunner(verbosity=2).run(suite)