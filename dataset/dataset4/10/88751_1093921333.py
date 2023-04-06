import csv
from pathlib import Path


def main():
    with Path('test.csv').open('rt') as csv_file:
        csv.register_dialect('my_dialect', quotechar='"', delimiter=',',
                             quoting=csv.QUOTE_ALL, skipinitialspace=True)
        reader = csv.DictReader(csv_file, dialect='my_dialect')
        for row in reader:
            print(row)


if __name__ == '__main__':
    main()