data = """<script type="text/javascript">
//<![CDATA[
function foo() {
document.write('"></' + 'script>');}
//]]>
</script>"""

from HTMLParser import HTMLParser
parser = HTMLParser()
parser.feed(data)