import bisect

fin = open('words.txt')
t = []

for line in fin:
    t.append(line.strip())

print(bisect.bisect(t,'musefully'))