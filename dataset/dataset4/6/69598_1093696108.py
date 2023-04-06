def __floordiv__(a, b):
        """a // b"""
        if isinstance(b, numbers.Complex) or hasattr(b, '__rtruediv__'):
            fr = a / b
            if fr != NotImplemented:
                return math.floor(a / b)
            else:
                return NotImplemented
        else:
            return NotImplemented