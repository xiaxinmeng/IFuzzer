import csv

with open("input.csv", "rb") as input, open("output.csv", "wb") as output:
    reader = csv.reader(input)
    writer = csv.writer(output)

    for row in reader:
        writer.writerow("data") # this writes out nothing
    
    writer.writerow("more data") # this writes out something