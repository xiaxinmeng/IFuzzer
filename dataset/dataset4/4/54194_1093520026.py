matcher = difflib.SequenceMatcher(a='aaaaaaaabc', b='aaaaaaaadc')
print(list(matcher.get_matching_blocks()))
# This should print the same thing, but it does not:
print(list(matcher.get_matching_blocks()))

print(matcher.get_opcodes())
print(list(matcher.get_grouped_opcodes()))
# This should print the same thing as the previous get_opcodes()
# list, but it does not:
print(matcher.get_opcodes())