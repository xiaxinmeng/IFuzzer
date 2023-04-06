from asyncio import test_utils
 
class Test(test_utils.TestCase):

    def setUp(self):
        super().setUp()
        self.loop = self.new_test_loop()

    def test_wrongly_scheduled(self):
        # this is a simple, and maybe mistaken, coroutine
        async def ag():
            yield None
        
        _ = self.loop.create_task(ag())
        test_utils.run_once(self.loop)