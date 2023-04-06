class C:
  def __getattr__(self, a): return self.x

C()