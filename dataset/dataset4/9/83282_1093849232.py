import unittest
class TestHangsForever(unittest.IsolatedAsyncioTestCase):
    async def test_hangs_forever(self):
        raise BaseException("Hangs forever")
if __name__ == "__main__":
    import unittest
    unittest.main()