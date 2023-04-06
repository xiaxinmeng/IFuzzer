with open(filename, "rt") as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=csv_delimiter)
        filednames = csv_reader.fieldnames