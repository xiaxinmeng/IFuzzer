import multiprocessing.managers, os, sys, time

if __name__ == '__main__':
    address = ("127.0.0.1", 54321)

    class TestManager(multiprocessing.managers.BaseManager):
        pass

    if sys.argv[1] == 'server':

        class TestClass(object):
            def test_method(self):
                print("In test_method")
                return "TEST"

        TestManager.register("Test", TestClass)
        manager = TestManager(address = address, authkey = "1234".encode("utf-8"))
        print('waiting...')
        manager.get_server().serve_forever()