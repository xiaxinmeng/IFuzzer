@skipUnless(is_cypthon and c_foo)
class CFooTests(PythonTest):
   ...

@skipUnless(is_jython and j_foo)
class JFooTests(PythonTest):
   ...