pure_comments_or_blank = True

for line in source:
    line = line.strip()
    if line and line[0] != '#':
        pure_comments_or_blank = False
        break

if pure_comments_or_blank:
    if symbol != "eval":
        source = "pass"