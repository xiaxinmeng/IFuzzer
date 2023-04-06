class D:
    def __get__(self, instance, owner):
       del C.d
       # There are now no strong references to self
       self.whatever # Access to freed memory