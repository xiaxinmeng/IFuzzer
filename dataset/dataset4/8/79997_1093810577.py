with open("conf-csv", "r") as csvfile:
    csv.register_dialect("comma_and_ws", skipinitialspace=True)
    csv_dict_reader = csv.DictReader(csvfile, dialect="comma_and_ws")
    for line in csv_dict_reader:
        print(line)