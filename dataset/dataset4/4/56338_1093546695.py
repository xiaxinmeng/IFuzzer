import sys
import xml.dom

doc = xml.dom.getDOMImplementation().createDocument(None, 'xml', None)
doc.firstChild.appendChild(doc.createElement('element00'))

element01 = doc.createElement('element01')
element01.setAttribute('attribute', "script><![CDATA[alert('script!');]]></script>")
doc.firstChild.appendChild(element01)

element02 = doc.createElement("script><![CDATA[alert('script!');]]></script>")
doc.firstChild.appendChild(element02)

element03 = doc.createElement("new line \n")

element03.setAttribute('attribute-name','new line \n')
doc.firstChild.appendChild(element03)