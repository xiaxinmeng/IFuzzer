class C: pass

object.__new__(C, 1)
C.__new__(C, 1)