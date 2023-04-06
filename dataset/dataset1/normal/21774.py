from xml.dom import minidom
dom = minidom.parseString("<a>1</a>")
pi = dom.createProcessingInstruction('xml-stylesheet',
                                     'type="text/xsl" href="mystyle.xslt"')
pi.nodeValue = "4"
