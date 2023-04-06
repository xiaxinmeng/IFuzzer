
import csv
with open("abc.csv", "w") as f:
   data = [b'\xc2a9', b'\xc2a9']
   w = csv.writer(f)
   w.writerow(data)
