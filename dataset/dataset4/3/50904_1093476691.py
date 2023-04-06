looking_for = None
for el in etree.getiterator(tag_or_path):
    looking_for = el
    break