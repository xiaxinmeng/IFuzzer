from xml.dom import minidom

html = """<html>
  <body>
    <!-- <img src="/images/obraz--super.jpg"/> -->
  </body>
</html>"""


minidom.parseString(html)