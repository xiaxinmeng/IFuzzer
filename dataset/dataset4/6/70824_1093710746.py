class Bla:
    def __del__(self):
        try:
            import xxxx
        except Exception as exc:
            print("import error: [%s] %r" % (type(exc), exc))

bla = Bla()