def escape_glob(path):
    transdict = {
            '[': '[[]',
            ']': '[]]',
            '*': '[*]',
            '?': '[?]',
            }
    rc = re.compile('|'.join(map(re.escape, transdict)))
    return rc.sub(lambda m: transdict[m.group(0)], path)