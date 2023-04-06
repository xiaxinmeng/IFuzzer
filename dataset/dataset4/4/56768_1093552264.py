for line in gzip.open('notes.txt', 'r', encoding='latin-1'):
    print(line.rstrip())