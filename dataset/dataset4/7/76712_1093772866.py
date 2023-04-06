class Foo(gdb.Command):

    def __init__(self):
        gdb.Command.__init__(self                     \
                , name            = 'n'               \
                , command_class   = gdb.COMMAND_USER  \
                , completer_class = gdb.COMPLETE_NONE \
                , prefix          = True)

    def invoke(self, arg, from_tty):
        output = gdb.execute(command='next',from_tty=False, to_string=True)
        print(output is None)
        print(output == '')

Foo()