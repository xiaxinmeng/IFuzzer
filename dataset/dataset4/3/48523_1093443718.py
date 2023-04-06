class C:
    def __init__(self):
        self.action = self.action_GO
        # cycle: the object's dict now contains a bound method 
        # which references the object
    def action_GO(self):
        print("GO")