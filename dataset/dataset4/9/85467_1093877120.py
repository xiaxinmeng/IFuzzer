
class Meta(type):
    def __setattr__(cls, key, value):
        type.__setattr__(cls, key, value)

class OtherClass:
    pass


class DefaultMeta(OtherClass, Meta):
    pass

obj = DefaultMeta('A', (object,), {})
obj.test = True
print(obj.test)
