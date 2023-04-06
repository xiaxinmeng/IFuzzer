class ReusableGenerator():
    def __init__(self,g): self.g = g
    def __iter__(self):   return self.g()

col2_re = ReusableGenerator(lambda: (a[2] for a in A)) # I want this!