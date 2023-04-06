class coop_OrderedDict(OrderedDict):
    """
    A cooperative version of OrderedDict
    """
    def __setitem__(self, k, v, **kwargs):
        # OrderedDict calls dict.__setitem__ directly skipping over LoggingDict
        # fortunately we can control this with dict_setitem keyword argument

        # calculate OrderedDict's real parent instead of skipping right to dict.__setitem__
        # though depending on the hierarchy it may actually be dict.__setitem__
        m = super(OrderedDict, self).__setitem__
        # dict_setitem wants an unbound method
        unbound_m = m.im_func
        return super(coop_OrderedDict, self).__setitem__(k, v, dict_setitem=unbound_m)