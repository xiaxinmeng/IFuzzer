
import unittest
from time import sleep, time
from multiprocessing import Pool

def slow(x):
    sleep(x)
    
# blocking sleep for 0, 1, 2, 3 seconds, concurrently
def together():
    with Pool(4) as p:
        p.map(slow, range(4))

class TestConcurrent(unittest.TestCase):
    # this is how you do it today
    def test_today(self):
        start = time()
        together()
        end = time()
        duration = end - start
        self.assertGreaterEqual(duration, 2)
        # max should be 3 seconds, plus some overhead
        # if together() called slow() in series,
        # total duration would be 0 + 1 + 2 + 3 = 6 > 4
        self.assertLessEqual(duration, 4) 
        
    # this is how I want to do it
    def test_simpler(self):
        with self.assertDuration(min=2, max=4):
            together()
