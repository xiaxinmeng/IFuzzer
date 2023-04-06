def outer():
  a=set()
  def inner():
    a.update(set(["A"]))
  inner()
  return a

print(outer())