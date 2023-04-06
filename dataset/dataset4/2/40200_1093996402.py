class excel(Dialect):
    delimiter = ','
    quotechar = '"'
    doublequote = True
    skipinitialspace = False
    if sys.platform == "win32":
        lineterminator = '\n'
    else:
        lineterminator = '\r\n'
    quoting = QUOTE_MINIMAL