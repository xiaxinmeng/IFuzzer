class unix_dialect(Dialect):
    """Describe the usual properties of unix-generated CSV files."""
    delimiter = ','
    quotechar = '"'
    doublequote = True
    skipinitialspace = False
    lineterminator = '\n'
    quoting = QUOTE_ALL
register_dialect("unix_dialect", unix_dialect)