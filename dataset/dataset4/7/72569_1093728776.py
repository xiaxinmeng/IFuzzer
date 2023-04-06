def __hash__(self):
    return hash(self.thing1) ^ hash(self.thing2) ^ hash(self.thing3)