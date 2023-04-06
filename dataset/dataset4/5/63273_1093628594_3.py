class Class:
    @property
    def __name__(self):
        return 'override'

c = Class()

print(c.__name__)