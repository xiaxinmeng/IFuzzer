class C(ValueError, OSError):pass
c = OSError.__new__(C)
str(c)
