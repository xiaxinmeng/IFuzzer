# Strip whitespace after insert point.
while text.get("insert") in " \t":
    text.delete("insert")