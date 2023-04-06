class ProcNet:
    pass

for proto in ('icmp', 'icmp6', 'raw', 'raw6', 'tcp', 'tcp6', 'udp', 'udp6', 'udplite', 'udplite6'):
    @cached_property
    def prop(self, *, proto=proto):
        with open(os.path.join("/proc/net", proto)) as file:
            return file.read()
    setattr(ProcNet, proto, prop)
    prop.__set_name__(ProcNet, proto)