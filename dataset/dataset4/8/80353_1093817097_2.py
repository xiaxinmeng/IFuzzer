import csv

data = [[1, 2, 3], [4, 5, 6]]

with open('test.csv', 'w') as fout:
    csv.writer(fout, lineterminator='\n').writerows(data)

with open('test.csv', 'r') as fin:
    data2 = list(csv.reader(fin))
    
print(data, data2, sep='\n')