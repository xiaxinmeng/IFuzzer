class Key:
    def __eq__(self, other):
        return self is other or random.getrandbits(1)
    def __hash__(self):
        return random.getrandbits(1)