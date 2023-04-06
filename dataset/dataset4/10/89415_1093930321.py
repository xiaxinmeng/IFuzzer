if not hasattr(socket, "IP_UNBLOCK_SOURCE"):
    setattr(socket, "IP_UNBLOCK_SOURCE", 37)
if not hasattr(socket, "IP_BLOCK_SOURCE"):
    setattr(socket, "IP_BLOCK_SOURCE", 38)
if not hasattr(socket, "IP_ADD_SOURCE_MEMBERSHIP"):
    setattr(socket, "IP_ADD_SOURCE_MEMBERSHIP", 39)
if not hasattr(socket, "IP_DROP_SOURCE_MEMBERSHIP"):
    setattr(socket, "IP_DROP_SOURCE_MEMBERSHIP", 40)