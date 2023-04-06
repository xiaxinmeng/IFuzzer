import xml.sax

data = b"""<main>
    <sub
        attr="1"
        id="name"
        >
        <subsub />
    </sub>
</main>"""


class MyHandler(xml.sax.handler.ContentHandler):

    def startElement(self, name, attrs):
        if name == "sub":
            print("open", name, self._locator.getLineNumber(), self._locator.getColumnNumber())
            
    def endElement(self, name):
        if name == "sub":
            print("close", name, self._locator.getLineNumber(), self._locator.getColumnNumber())

xml.sax.parseString(data, MyHandler())