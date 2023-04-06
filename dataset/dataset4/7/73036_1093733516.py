import pprint
import sys

pprint.pprint(sys.version_info)

class MyPrettyPrinter(pprint.PrettyPrinter):
    def format(self, object, context, maxlevels, level):
        if isinstance(object, int):
            return hex(object), True, False
        else:
            return pprint.PrettyPrinter.format(self, object, context, maxlevels, level)