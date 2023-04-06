class Stock(Structure):
    __signature__ = make_signature(['name', 'shares', 'price'])
    def __init__(self, *args, **kwds):
        super(Stock, self).__init__(*args, **kwds)
    __init__.__signature__ = __signature__