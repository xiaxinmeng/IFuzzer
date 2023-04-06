# It was a syntax error; show exactly where the problem was found.
filename = self.filename or "<string>"
lineno = str(self.lineno) or '?'
yield '  File "{}", line {}\n'.format(filename, lineno)