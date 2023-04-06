
import json
a = [object()] * 10
def crasher(obj):
    del a[-1]

json.dumps(a, default=crasher)
