class IndentAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        indent = kwargs.pop(indent, 1)
        return ' ' * indent + msg, kwargs