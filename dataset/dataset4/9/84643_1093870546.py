import csv
lst = ['"A,"h"e, ","E","DC"']

csv_list = csv.reader(lst)
for idx, col in enumerate(next(csv_list)):
    print(idx, repr(col))