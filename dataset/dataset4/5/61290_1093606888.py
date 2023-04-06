from xml.etree.ElementTree import *
register_namespace('svg', 'http://www.w3.org/2000/svg')
svg = ElementTree(XML("""
<svg width="12cm" height="4cm" viewBox="0 0 1200 400" xmlns="http://www.w3.org/2000/svg" version="1.1">
<rect x="1" y="1" width="1198" height="398" fill="none" stroke="blue" stroke-width="2" />
</svg>
"""))
svg.write('simple_new.svg',encoding='UTF-8',default_namespace='svg')