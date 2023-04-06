
import csv
fp = open('test.csv', 'w')
w = csv.writer(fp)
w.writerow(['1'])
w.writerow([''])
fp.close()
