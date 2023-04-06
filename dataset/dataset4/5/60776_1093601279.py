class Foo(object):
    def __init__(self):
        super(Foo, self).__init__()
        print('Foo constructor')
        self.param1 = 'foo param1'


class Bar(Thread, Foo):
    def __init__(self):
        super(Bar, self).__init__()
        print('Bar constructor')
        self.another_param1 = "bar another_param1"

    def run(self):
        print("Running (%s - %s)" % (self.another_param1, self.param1))


if __name__ == '__main__':
    threads = []
    for i in range(1, 10):
        thread = Bar()
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()