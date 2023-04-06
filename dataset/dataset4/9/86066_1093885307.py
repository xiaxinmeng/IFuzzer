import xml.etree.ElementTree as ET
xml="""
<X xmlns="http://soap.sforce.com/2006/04/metadata">
    <Y targets="lightning__AppPage,lightning__HomePage"></Y>
</X>"""
print(ET.canonicalize(xml))