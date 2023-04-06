def __floordiv__(a, b):
        """a // b"""
        if isinstance(b, numbers.Complex):
            return math.floor(a / b)
        else:
            return NotImplemented