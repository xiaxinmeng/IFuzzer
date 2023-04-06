def fullmatch(pattern, string):
    match = re.match(pattern, string)
    if match:
        if match.start() == 0 and match.end() == len(string):
            return match
        else:
            return None
    else:
        return None