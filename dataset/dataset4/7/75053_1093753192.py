class Test(unittest.TestCase):
    def setUp(self):
        self.root = tkinter.Tk()

    def test_test(self):
        self.root.bind('<KeyRelease-Up>', lambda x: print('testing'))
        self.root.update()
        self.root.event_generate('<KeyRelease-Up>')