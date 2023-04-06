class tb_entity(namedtuple('tb_entity', 'filename lineno name line')):
    def __new__(cls, filename, lineno, name, line, frame=None):
        self = super().__new__(cls, filename, lineno, name, line)
        self.frame = frame
        return self