import csv
writer = csv.writer(file("some.csv", "w"))
for row in someiterable:
    writer.writerow(row)