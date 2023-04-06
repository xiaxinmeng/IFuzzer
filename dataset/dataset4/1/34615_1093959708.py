def xmlreplace(encoding, unicode, pos, state):
   return (u"&#%d;" % ord(uni[pos]), pos+1)

import codec

codec.registerError("xmlreplace",xmlreplace)