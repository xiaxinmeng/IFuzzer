buffer = b"a" * 8191 + b"\\r\\n"

with open("bug_csv.csv", "wb") as f:
    f.write(buffer)

with open("bug_csv.csv", encoding="unicode_escape", newline="") as f:
    f.readline()