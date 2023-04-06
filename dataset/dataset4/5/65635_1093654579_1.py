import importlib.machinery
loader = importlib.machinery.SourceFileLoader("what.ever", "foo.py")
my_module = loader.load_module("what.ever")