class ClassWithDel:
    def __del__(self):
        print('__del__ called')

a = ClassWithDel()
a.link = a

raise SystemExit(0)