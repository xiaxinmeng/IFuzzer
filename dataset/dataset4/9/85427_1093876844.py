class MultipleArgumentError(ArgumentError):

    def __init__(self, arguments, message):
        self.argument_names = filter([_get_action_name(arg) for arg in arguments], lambda name: name)
        self.message = message

    def __str__(self):
        if self.argument_names is None:
            format = '%(message)s'
        else:
            format = 'argument %(argument_names): %(message)s'
        return format % dict(message=self.message,
                             argument_names=', '.join(self.argument_name))