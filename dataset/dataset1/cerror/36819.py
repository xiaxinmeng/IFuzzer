import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

# The interpreter will segfault on the first call
codecs.utf_16_encode("\udc80", "add_one_codepoint")

# Each of the calls below also cause segfaults
codecs.utf_32_encode("\udc80", "add_one_codepoint")
codecs.utf_16_encode("\udc80", "add_utf16_bytes")
codecs.utf_32_encode("\udc80", "add_utf32_bytes")
