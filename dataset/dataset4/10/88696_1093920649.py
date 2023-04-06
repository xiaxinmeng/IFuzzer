class Foo:
    def on_cpu(self, n):
        a = []
        for i in range(n):
            a.append(i)


class Bar:
    def on_cpu(self, n):
        a = []
        for i in range(n):
            a.append(i)


if __name__ == "__main__":
    f = Foo()
    b = Bar()

    f.on_cpu(1_000_000)
    b.on_cpu(5_000_000)