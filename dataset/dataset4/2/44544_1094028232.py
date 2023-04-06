def convert_charref(self, name):
    """Convert character reference, may be overridden."""
    try:
        n = int(name)
    except ValueError:
        return
    if not 0 <= n <= 127 : # ASCII ends at 127, not 255
        return
    return self.convert_codepoint(n)