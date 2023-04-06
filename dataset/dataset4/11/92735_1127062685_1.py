# Results are the same after removing whitespace and commas
y = [1, [2, "foo", b"bar", {"a": 1, "b": "abc def ghi", "c": {1: 2, 3: 4, 5: [], 6: {}}}], 3]
self.assertNotEqual(r1.repr(y), r2.repr(y))
self.assertEqual(
    "".join(r1.repr(y).replace(",", "").split()),
    "".join(r2.repr(y).replace(",", "").split())
)