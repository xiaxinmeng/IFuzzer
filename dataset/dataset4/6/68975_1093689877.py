def make_dialect(delimiter):
    class Dialect(csv.excel):
        pass
    Dialect.delimiter = delimiter
    return Dialect

def sniff(sample):
    count, delimiter = max(
        ((sample.count(delim), delim) for delim in ",\t|;"),
        key=operator.itemgetter(0))
    if count == 0:
        if " " in sample:
            delimiter = " "
        else:
            raise csv.Error("Could not determine delimiter")
    return make_dialect(delimiter)