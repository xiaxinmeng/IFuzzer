import timeit

s1 = """
text = ""
for i in range(1,50000):
  text += "12345678901234567890"
"""
print("str cat 20: {0}s".format(timeit.timeit(s1,number=1)))

s2 = """
d = dict()
d["text"] = ""
for i in range(1,50000):
  d["text"] += "12345"
"""
print("dict cat 5: {0}s".format(timeit.timeit(s2,number=1)))

s3 = """
d = dict()
d["text"] = ""
for i in range(1,50000):
  d["text"] += "1234567890"
"""
print("dict cat 10: {0}s".format(timeit.timeit(s3,number=1)))


s4 = """
d = dict()
d["text"] = ""
for i in range(1,50000):
  d["text"] += "12345678901234567890"
"""
print("dict cat 20: {0}s".format(timeit.timeit(s4,number=1)))