fields = ['a','b','c']
w = csv.DictWriter(fid, fields)
w.writerow(dict(zip(fields, fields)))
for row in rows:
    w.writerow(row)