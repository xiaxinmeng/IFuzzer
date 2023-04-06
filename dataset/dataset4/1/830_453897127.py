
from collections import deque
from json import dumps, JSONEncoder

class JSONEncoderSupportingArbitraryIterators(JSONEncoder):
    def default(self, o):
        try:
            iterable = iter(o)
        except TypeError:
            pass
        else:
            return list(iterable)
        # Let the base class default method raise the TypeError
        return JSONEncoder.default(self, o)

dumps(deque(range(10)), cls=JSONEncoderSupportingArbitraryIterators)
