output_lines = []
for line in difflib.ndiff(a, b):
    if len(output_lines) > self.maxDiff:
        break
    output_lines.append(line)