#!/usr/bin/python
class M:
  b = 0
  def __del__(self):
    M.b = 0

a1 = M()