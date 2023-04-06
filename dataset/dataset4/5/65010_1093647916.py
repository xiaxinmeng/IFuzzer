class MyFloat(float):
    def __format__(self, fmt):
        s = float.__format__(self, fmt)
        if s[1] == '0':
            return s[0] + s[2:]
        return s