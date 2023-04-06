class Bad(P):  # <- this is _no_ a protocol, just a nominal class
    pass       # explicitly subclassing P

class Good(P, Protocol):  # <- this is a subprotocol that
    pass                  # happened to be identical to P