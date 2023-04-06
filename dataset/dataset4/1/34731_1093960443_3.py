from xml.sax import saxutils 
gen = saxutils.XMLGenerator() 
gen.startDocument() 
gen.startElement('spam', {'width': '5\'3"'}) 