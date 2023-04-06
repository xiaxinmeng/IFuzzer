DATA = '''<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank updated="yes">5</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank updated="yes">69</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
'''

import xml.etree.ElementTree as ET

root = ET.XML(DATA)
print(root)
for XP in (['./country'] +
           ['./country[%d]' % i for i in range(-1, 5)] +
           ['./country[last()%+d]' % i for i in range(-3, 5)]):
    print('{:20}'.format(XP), [elem.get('name') for elem in root.findall(XP)])