class C:
    ...

    def __hash__(self):
        return hash((v for k, v in sorted(self.__dict__.items())))