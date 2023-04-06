import csv
import io


f = io.StringIO()

writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
writer.writerow(['asdf', 1, True])

f.seek(0)
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    print(row)