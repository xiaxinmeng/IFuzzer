class _WrapForRecv:
    def __init__(self, obj):
        self.__obj = obj

    def __getattr__(self, name):
        if name == "recv": name = "read"
        return getattr(self.__obj, name)