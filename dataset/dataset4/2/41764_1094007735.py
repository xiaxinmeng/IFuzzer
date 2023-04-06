def test_islice():
  it = iter(range(10))
  a = list(islice(it, 0,3))
  next = it.next()
  assert next == 3

test_islice()