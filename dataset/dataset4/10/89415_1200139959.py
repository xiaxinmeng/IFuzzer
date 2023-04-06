
platform = platform.system()
if (platform == "Windows"):
    if not hasattr(socket, "IP_UNBLOCK_SOURCE"):
        setattr(socket, "IP_UNBLOCK_SOURCE", 18)
    if not hasattr(socket, "IP_BLOCK_SOURCE"):
        setattr(socket, "IP_BLOCK_SOURCE", 17)
    if not hasattr(socket, "IP_ADD_SOURCE_MEMBERSHIP"):
        setattr(socket, "IP_ADD_SOURCE_MEMBERSHIP", 15)
    if not hasattr(socket, "IP_DROP_SOURCE_MEMBERSHIP"):
        setattr(socket, "IP_DROP_SOURCE_MEMBERSHIP", 16)
elif (platform == 'Darwin'):
    if not hasattr(socket, "IP_UNBLOCK_SOURCE"):
        setattr(socket, "IP_UNBLOCK_SOURCE", 73)
    if not hasattr(socket, "IP_BLOCK_SOURCE"):
        setattr(socket, "IP_BLOCK_SOURCE", 72)
    if not hasattr(socket, "IP_ADD_SOURCE_MEMBERSHIP"):
        setattr(socket, "IP_ADD_SOURCE_MEMBERSHIP", 70)
    if not hasattr(socket, "IP_DROP_SOURCE_MEMBERSHIP"):
        setattr(socket, "IP_DROP_SOURCE_MEMBERSHIP", 71)
else:
    if not hasattr(socket, "IP_UNBLOCK_SOURCE"):
        setattr(socket, "IP_UNBLOCK_SOURCE", 37)
    if not hasattr(socket, "IP_BLOCK_SOURCE"):
        setattr(socket, "IP_BLOCK_SOURCE", 38)
    if not hasattr(socket, "IP_ADD_SOURCE_MEMBERSHIP"):
        setattr(socket, "IP_ADD_SOURCE_MEMBERSHIP", 39)
    if not hasattr(socket, "IP_DROP_SOURCE_MEMBERSHIP"):
        setattr(socket, "IP_DROP_SOURCE_MEMBERSHIP", 40)
   