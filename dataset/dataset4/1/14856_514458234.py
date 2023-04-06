from xml.etree import ElementTree
while True: ElementTree.fromstring("<a>text<!--c1-->a<!--c2-->b<!--c3-->foo</a>").text