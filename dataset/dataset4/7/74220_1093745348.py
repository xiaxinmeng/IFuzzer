def close_quote(line):
    if line.count('"') % 2:
        line = line.rstrip("\n") + '"\n'
    return line

with open("data.csv") as f:
    for row in csv.reader(map(close_quote, f)):
        print(row)