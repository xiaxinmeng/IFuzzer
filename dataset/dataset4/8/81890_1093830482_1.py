filename = "csvFile.csv"
from csv import DictReader, DictWriter
import csv
with open(filename, mode='w') as output_file:
    outcsv = csv.writer(output_file, delimiter=',', lineterminator=";")
    outcsv.writerow(['John Cleese', 'CEO', 'March'])
    outcsv.writerow(['Graham Chapman', 'CFO', 'November'])
    outcsv.writerow(['Terry Jones', 'Animation', 'March'])
    outcsv.writerow(['Eric Idle', 'Laugh Track', 'November'])
    outcsv.writerow(['Michael Palin', 'Snake Wrangler', 'March'])

with open(filename, mode='r') as input_file:
    csv_reader = csv.reader(input_file, delimiter=',', lineterminator=";")
    for row in csv_reader:
        print(row)