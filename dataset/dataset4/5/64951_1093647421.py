import difflib
# either
class MyDiff: pass  # not really ;-)
# MyDiff might or might not subclass SequenceMatcher
difflib.SequenceMatcher = MyDiff
# or
def f(self, *args): pass  # again, not really
difflib.SequenceMatcher.somemethod = f
# either way, use difflib functions with alternate matcher.