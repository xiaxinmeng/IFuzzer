class Interpolation:
    """Dummy interpolation that passes the value through with no changes."""

    def before_read(self, parser, section, option, value):
        return value