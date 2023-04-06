w = csv.DictWriter(fid, ['a','b','c'], header = True)
for row in rows:
    w.writerow(row)