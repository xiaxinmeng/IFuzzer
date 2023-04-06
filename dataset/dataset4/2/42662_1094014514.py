class MyPrettyPrinter(pprint.PrettyPrinter):
    def format(self, object, context, maxlevels, 
level):
        if isinstance(object, int):
            return hex(object), True, False
        else:
            return pprintmod.PrettyPrinter.format(
                self, object, context, maxlevels, 
level)