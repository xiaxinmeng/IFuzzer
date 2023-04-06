################################
# super_ok.py
class A(object):
  def foo(self):
    return super()
    # comment the closure below
    # & SystemError goes away
    # lambda: self
A().foo()
################################