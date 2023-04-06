import select
a = []
class F:
    def fileno(self):
        del a[-1]
        return 1