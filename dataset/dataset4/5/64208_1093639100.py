class qproperty(property):
    # Fix for ipython ? and ?? (%pdef, %psource)
    # Omitting the class doc string prevents ipython from showing the
    # doctoring for the property builtin class; I suspect this is a
    # bug.
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        super(qproperty, self).__init__(fget, fset, fdel, doc)
        self.__wrapped__ = fget

# Overwrite property with qproperty so that in the future this hack might
# be easily removed.
property = qproperty