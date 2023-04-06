
import csv
fp = open('test.csv', 'w')
w = csv.writer(fp, dialect=None)
w.writerow(['', ''])
w.writerow(['3', 'a'])
fp.close()
