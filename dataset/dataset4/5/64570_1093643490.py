import datetime

class my_dt(datetime.datetime):
    def __new__(cls, *args, **kwargs):
        print('In my_dt.__new__')
        return datetime.datetime.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print('In my_dt.__init__')
        super(my_dt, self).__init__()

dt = datetime.datetime.now()

print('Create a my_dt')
t = my_dt(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond, dt.tzinfo)


print('Calling replace')
t2 = t.replace(tzinfo=None)
print('Got a %r' % type(t2))