
with open("abc.csv", "w", encoding='utf-8') as f:
    data = [b'\x41']
    w = csv.writer(f)
    w.writerow(data)
with open("abc.csv", "r") as f:
    rows = csv.reader(f)
    for row in rows:
        print(row[0]) # prints b'A'
