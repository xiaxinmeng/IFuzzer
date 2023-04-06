#pyrebug.py:
import re
urlrebug=re.compile("""
	(.*?)://			#scheme
	(
		(.*?)			#user
		(?:
			:(.*)		#pass
		)?
	@)?
	(.*?)				#addr
	(?::([0-9]+))?			#port
	(/.*)?$				#path
""", re.VERBOSE)

testbad='foo://bah:81/pth'