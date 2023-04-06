class Parent():
  def __str__(self):
    return "Parent"

class Child(Parent):
  def foo(self):
    s = super(Child, self)
    print(s.__str__())
    print(str(s))


c = Child()
c.foo()