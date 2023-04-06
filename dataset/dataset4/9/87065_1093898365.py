class FlipFlop:
    def __init__(self):
        self.val = random.choice((True, False))
    def __bool__(self):
        self.val = not self.val
        return self.val