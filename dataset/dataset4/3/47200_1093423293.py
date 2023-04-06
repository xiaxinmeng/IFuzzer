from xml.etree import ElementTree as eltree

def handler(req):
    body = """<?xml version='1.0' encoding='utf-8'?>
<collection uuid="~01edc22c1628e711ddb20220296b032019"
href="http://localhost:8888/ws/dataset/~01edc22c1628e711ddb20220296b032019">
  <name>Service_offerings query at 2008-05-23 12:47:28.038233</name>
</collection>"""

    response_elem = eltree.XML(body)
    return 0