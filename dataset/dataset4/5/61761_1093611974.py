def support_hybrid_ip_v4_v6():
    # Note: IPPROTO_IPV6 constant is broken on Windows, see:
    # http://bugs.python.org/issue6926
    sock = None
    try:
        if not socket.has_ipv6:
            return False
        sock = socket.socket(socket.AF_INET6)
        return not sock.getsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY)
    except (socket.error, AttributeError):
        return False
    finally:
        if sock is not None:
            sock.close()