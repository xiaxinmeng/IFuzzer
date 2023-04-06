class _ProtocolMeta(ABCMeta):
    # …
    def __instancecheck__(cls, instance):
        if super().__instancecheck__(instance):
            # Short circuit for direct inheritors
            return True
        else:
            # … existing implementation that checks method names, etc. …
            return False