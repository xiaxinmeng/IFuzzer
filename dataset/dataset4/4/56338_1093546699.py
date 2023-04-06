element01 = doc.createElement('element01')
element01.setAttribute('attribute', "script><![CDATA[alert('script!');]]></script>")
doc.firstChild.appendChild(element01)