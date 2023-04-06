from xml.dom import minidom

data = b'''
<rss xmlns:atom="http://www.w3.org/2005/Atom" version="2.0">
  <channel>
    <link>https://example.com/blog/</link>
    <atom:link href="https://example.com/rss2/" rel="self"></atom:link>
    <item>
      <link>https://example.com/blog/1/</link>
    </item>
  </channel>
</rss>'''

doc = minidom.parseString(data)
for link in doc.getElementsByTagName('link'):
    print(link._attrs)