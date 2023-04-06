class BB(object):
    def __init__(self):pass
    def print_b(self):pass
    def print_bb(self,tsk_id):pass


bMock = Mock(return_value=Mock(spec=BB))
bMock().print_bb(20)
bMock().assert_has_calls([call.print_bb(20)])