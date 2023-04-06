def tokenize(string, seps):
    return re.split("|".join(map(re.escape, seps)), string)