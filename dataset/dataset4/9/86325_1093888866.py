import asyncio
import unittest
from unittest import TestCase
from unittest.mock import *

def sync_func():
    raise Exception

class Test(TestCase):

    def test_simultaneous_mocks_sync(self):
        patcher1 = patch(f"{__name__}.sync_func")
        patcher2 = patch(f"{__name__}.sync_func")

        patcher1.start()
        print(sync_func())

        patcher2.start()
        print(sync_func())

        breakpoint()
        patcher1.stop()
        with self.assertRaises(Exception):
            sync_func()

        breakpoint()
        patcher2.stop()

        with self.assertRaises(Exception): # Fails, mock is restored!
            sync_func()

if __name__ == "__main__":
    unittest.main()