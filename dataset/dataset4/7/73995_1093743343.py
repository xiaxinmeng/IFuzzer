class LenientIO(io.BytesIO):
    """
    A version of BytesIO that can accept unicode or
    bytes. See http://bugs.python.org/issue29809
    """
    def write(self, value):
        if isinstance(value, six.text_type):
            value = value.encode('utf-8')
        super(LenientIO, self).write(value)