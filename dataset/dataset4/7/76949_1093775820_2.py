class StatefulThing(Stateful):
    class StateA:
        """First state mixin."""

        def say_hello(self):
            print("Hello!")
            self.hello_count += 1
            self._set_state(self.StateB)
            return True

        def say_goodbye(self):
            print("Another goodbye?")
            return False

    class StateB:
        """Second state mixin."""

        def say_hello(self):
            print("Another hello?")
            return False

        def say_goodbye(self):
            print("Goodbye!")
            self.goodbye_count += 1
            self._set_state(self.StateA)
            return True

    # This one is required by Stateful.
    class InitState(StateA):
        """Third state mixin -- the initial state."""

        def say_goodbye(self):
            print("Why?")
            return False

    def __init__(self):
        self.hello_count = self.goodbye_count = 0

    def say_hello_followed_by_goodbye(self):
        self.say_hello() and self.say_goodbye()