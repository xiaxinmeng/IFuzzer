class NewType:
    def __mro_entries__(cls, bases):
        raise TypeError(f'Cannot subclass an instance of `NewType`')