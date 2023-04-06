class TestStuff(TestCase):
    def setUp(self):
        self.stack = ExitStack()

        self.stack.enter_context(my_context_manager())
        self.stack.enter_context(my_context_manager2())
        self.stack.enter_context(my_context_manager3())

        self.stack.enter()
        self.addCleanup(self.stack.exit)