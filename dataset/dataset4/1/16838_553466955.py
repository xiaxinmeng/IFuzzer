class ProcNet:
    def __new__(cls, *args, **kwargs):
        for proto in ('icmp', 'icmp6', 'raw', 'raw6', 'tcp', 'tcp6', 'udp', 'udp6', 'udplite', 'udplite6'):
            prop = cached_property(partial(cls._proto, proto=proto))
            setattr(cls, proto, prop)
            prop.__set_name__(cls, proto)
        return super().__new__(cls, *args, **kwargs)