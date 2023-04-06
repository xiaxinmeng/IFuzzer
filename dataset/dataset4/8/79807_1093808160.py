def load_file(filename):

    with open(filename, 'r', encoding='utf-8') as fin:
        header = fin.readline()
        print('Found ' + header)

        reader = csv.DictReader(fin)

        for row in reader:
            print(type(row), row)
            print('Beds {} '.format(row['beds']))