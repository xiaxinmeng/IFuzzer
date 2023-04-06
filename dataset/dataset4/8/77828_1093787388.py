def re_replace(string, mapping):
    def repl(m):
        return mapping[m[0]]
    pattern = '|'.join(map(re.escape, sorted(mapping, reverse=True)))
    return re.sub(pattern, repl, string)