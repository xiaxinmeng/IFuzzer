# paste the following at the interactive prompt:
pat = r"b{1, 3}\Z"
bool(re.match(pat, "bb")) # False
bool(re.match(pat, "b{1, 3}")) # True
bool(re.match(pat, "bb", re.VERBOSE)) # False
bool(re.match(pat, "b{1, 3}", re.VERBOSE)) # False
bool(re.match(pat, "b{1,3}", re.VERBOSE)) # True