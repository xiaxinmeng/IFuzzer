import re
text = 'ab\\'
exp = re.compile('a')
print(re.sub(exp, text, ''))