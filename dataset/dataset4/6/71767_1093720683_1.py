import csv
data = csv.DictReader(ascii) 
for line in data: print(line) #NULL Byte Error