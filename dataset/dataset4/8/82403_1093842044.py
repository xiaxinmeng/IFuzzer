class object:
    def __format__(self, format_spec):
        return format(str(self), format_spec)