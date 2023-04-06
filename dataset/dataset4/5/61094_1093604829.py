import xml.dom.minidom as minidom
document="""<a>
    <b>
        <c />
        <c />
    </b>
</a>""" 
dom = minidom.parseString(document)