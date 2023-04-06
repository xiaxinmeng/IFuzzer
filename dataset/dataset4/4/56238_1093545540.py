def message_contains(msg):
    class _MyExc(object):
        def __instancecheck__(self, exc):
            return msg in exc.args[0]
    return _MyExc