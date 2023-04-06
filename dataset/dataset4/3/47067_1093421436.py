events = xml.dom.pulldom.parse('file.xml')
for (event, node) in events:
    process(event, node)