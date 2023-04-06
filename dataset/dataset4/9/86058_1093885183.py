#Just run it in Python v3.8.6 of win7 32bit 
import xml.etree.ElementTree as ET 
xmlstr='''<root>
<a no="1"/>
<b/>
<c/>
</root>'''
etroot = ET.fromstring(xmlstr)
for ELEMchild in etroot:
    if ELEMchild.get("no") == "1" :
        etroot.remove(ELEMchild)       #so far so good
    print (ELEMchild.tag)
    #It should be :  "b /n c" or "a /n b /n c",I can live with it both.
    #But it is :  "a /n c".
    #The index of ELEMchild should not +1 when there was a remove method worked on one of the before ELEMs.
    #I was forced to use while and if to control the index +1/+0.
    #BTW,ELEM has no method returning index in siblings, which is buging me too.