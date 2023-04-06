
class TestMe:
    def __init__(self):
        self.item = {'akey': 42}
        self.again = self

x = TestMe()
### pylint error message here is
###    testme.py:11:6: E1101: Instance of 'dict' has no 'akey' member (no-member)
### The problem is with `x.item`, but pylint shows the column for `x`
print(x.item.akey > 2)

print(x.again.item.doesnotexist)
