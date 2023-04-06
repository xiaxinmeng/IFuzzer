def uuid4():
    """Generate a random UUID."""

    # When the system provides a version-4 UUID generator, use it.
    if _uuid_generate_random:
        _buffer = ctypes.create_string_buffer(16)
        _uuid_generate_random(_buffer)
        return UUID(bytes=_buffer.raw)
    ...