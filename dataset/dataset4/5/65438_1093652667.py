import mock

def myfunc():
   return 'hello'

m = mock.patch('__main__.myfunc').start()
m.return_value = 'firstmock'
myfunc()

m2 = mock.patch('__main__.myfunc').start()
m2.return_value = 'secondmock'
myfunc()

mock.patch.stopall()
myfunc()