
import csv
fp = open('test.csv', 'w')
w = csv.writer(fp)
w.writerow([''])
w.writerow(['1'])
fp.close()
