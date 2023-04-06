pat2 = r"b\{1, 3}\Z"
bool(re.match(pat2, "b{1, 3}")) # True