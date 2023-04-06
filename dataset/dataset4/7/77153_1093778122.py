class MyTest(TestCase):

    # I assume trio has something like this :)
    coroutine_runner = trio.run

    async def test_something_in_trio(self):
        self.assertTrue(1)