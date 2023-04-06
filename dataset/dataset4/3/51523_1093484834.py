import json, os
from StringIO import StringIO

def Validate( case ):
    try:
        l = json.loads( case[1] )
        print( "%s %s"%case )
    except:
        pass