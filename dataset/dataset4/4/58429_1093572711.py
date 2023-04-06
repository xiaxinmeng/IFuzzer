import re

text= "The cat ate the rat."
print("before: %s" % text)
m= re.search("The (\w+) ate the (\w+)", text)
text= "The %s ate the %s." % (m.group(2), m.group(1))
print("after : %s" % text)

text= "The cat ate the rat."
print("before: %s" % text)
text= re.sub("(\w+) ate the (\w+)", "\2 ate the \1", text)
print("after : %s" % text)