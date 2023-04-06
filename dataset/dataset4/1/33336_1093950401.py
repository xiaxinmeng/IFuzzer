from xml.dom import minidom
doc = minidom.Document()
root = doc.createElement('root') ; doc.appendChild( root )

elem = doc.createElement('leaf')
root.appendChild( elem )
root.appendChild( elem )