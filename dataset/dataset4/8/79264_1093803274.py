class M(type):
    def __instancecheck__(m, t):
        print('instancecheck(%s, %s)' % (m, t))
        return False                                    #   LIE!

Test = M('Test', ((object,)), {})

something = Test()

print('Does *NOT* call __instancecheck__:')
print('isinstance(something, Test): %s' % isinstance(something, Test))

print()
print('Does call __instancecheck__:')
print('isinstance(0, Test):         %s' % isinstance(0,         Test))