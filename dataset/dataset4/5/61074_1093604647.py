r = re.compile("abc")
s = "0123abcxyz"
match = r.search(s)
if match:
    print(match.start(), match.end())