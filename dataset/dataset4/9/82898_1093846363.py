import csv

fields = ["c", "d"]
with open('test.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=fields, extrasaction='raise')
    writer.writeheader()
    writer.writerow({"n": 1})