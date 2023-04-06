s5 = """
text = ""
for i in range(1,50000):
  text2 = text
  text += "12345678901234567890"
"""
print("str cat 20: {0}s".format(timeit.timeit(s5,number=1)))