def parse_multipart(fp, pdict):
    return FieldStorage(fp,environ=pdict)