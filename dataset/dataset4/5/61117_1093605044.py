with open(fp, mode='rt') as f:
    data = f.read()
tree, idmap = ET.XMLID(data)
print(ET.tostring(tree, method='text', encoding='unicode'))