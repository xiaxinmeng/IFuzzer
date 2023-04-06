from xml.etree import ElementTree
class MyTreeBuilder(ElementTree.TreeBuilder):
   def comment(self, data):
       self.start(ElementTree.Comment, {})
       self.data(data)
       self.end(ElementTree.Comment)
with open('c:/temp/t.xml', 'r') as f:
   xml = ElementTree.parse(
       f, parser=ElementTree.XMLParser(target=MyTreeBuilder()))
ElementTree.dump(xml)