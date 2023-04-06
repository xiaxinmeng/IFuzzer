# commented out until Fredrick's fix is checked in
def _testElementReprAndStrUnicodeNS():
    dom=Document()
    el=dom.appendChild(
	 dom.createElementNS( u"http://www.slashdot.org", u"slash:abc" ))