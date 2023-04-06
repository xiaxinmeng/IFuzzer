class Foo:
 def __iter__(self):
  print("iter")
  return iter([3, 5, 42, 69])

 def __len__(self):
  print("len")
  return 4