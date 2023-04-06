offset = lnotab[n]
if offset == 0:
    line = -1 # artificial
else:
    line_base = scan_table_to_find(n)
    line = offset + line_base