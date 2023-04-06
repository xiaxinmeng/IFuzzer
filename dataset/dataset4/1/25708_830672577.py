# Find all text with the "stdin" tag in the selected range
code_pieces = []
index = text.index("sel.first")
while tag_range := text.tag_nextrange("stdin", index, "sel.last"):
    index = tag_range[1]
    code_pieces.append(text.get(*tag_range))