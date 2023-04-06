with mock.patch.object(testmock.Something, 'meth', autospec=True):
    smth = testmock.Something()
    smth.meth(mock.sentinel.a, mock.sentinel.b, mock.sentinel.c, mock.sentinel.d)
    smth.meth.assert_called_once_with(mock.sentinel.a, mock.sentinel.b, mock.sentinel.c, mock.sentinel.d)