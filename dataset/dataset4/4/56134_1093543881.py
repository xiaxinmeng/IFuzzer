class NotebookTest(unittest.TestCase):

    def setUp(self):
        support.root_deiconify()
        self.nb = ttk.Notebook(padding=0)
        self.child1 = ttk.Label()
        self.child2 = ttk.Label()
        self.nb.add(self.child1, text='a')
        self.nb.add(self.child2, text='b')



    def test_traversal(self):
        self.nb.pack()
        self.nb.wait_visibility()

        self.nb.select(0)

        support.simulate_mouse_click(self.nb, 5, 5)
        self.nb.focus_force()
        self.nb.event_generate('<Control-Tab>')
        self.assertEqual(self.nb.select(), str(self.child2)) <~~~ HERE
        ...