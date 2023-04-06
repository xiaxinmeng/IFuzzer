def split_whitespace_ascii(s: str):
    return (pt.group(0) for pt in re.finditer(r"[A-Za-z']+", s))