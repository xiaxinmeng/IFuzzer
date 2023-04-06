import HTMLParser

p = HTMLParser.HTMLParser()
p.feed("""
<script>
<!--
bmD.write('</sc'+'ript>');
//-->
</script>
""")