import xml.etree.ElementTree as et
import StringIO
s = StringIO.StringIO("<a>x</a><a>y</a>")
elem1 = et.parse(s)
elem2 = et.parse(s)