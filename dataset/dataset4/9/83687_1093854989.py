def outer():
  a=set()
  def inner():
    a |= set(["A"])
  inner()
  return a

print(outer())