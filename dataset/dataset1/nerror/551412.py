class UserLong(object):
    def __pow__(self, *args):
        pass

coredump = 1

if not coredump:
   int.__mro__

pow(0, UserLong(), 0)
