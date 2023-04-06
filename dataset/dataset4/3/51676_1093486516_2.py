class BadStatusLine(HTTPException):
    def __init__(self, line):
        self.args = line,
        self.line = line

class HTTPException(Exception):
    # Subclasses that define an __init__ must call Exception.__init__
    # or define self.args.  Otherwise, str() will fail.
    pass