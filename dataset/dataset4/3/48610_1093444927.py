################################
# super_closure.py
class A(object):
  def foo(self):
    return super()
    # remove the closure below
    # & SystemError goes away ???
    lambda: self
A().foo()
################################