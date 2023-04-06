import re

pattern = re.compile("spam")
string = "Monty pythons"
for _ in range(1000000):
    re.search(pattern, string)