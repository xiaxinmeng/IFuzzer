class ExecTest:
    def public(self):
        h=None
        exec("h='It is public'")
        print(h)
        self._private()
    def _private(self):
        h=None
        exec("h='It is private'", globals(), locals())
        print(h)

h = None
exec("h='It is global'")
print(h)

e=ExecTest()
e.public()