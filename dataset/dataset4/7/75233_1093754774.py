class NamePage(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_page_name()
        self.load_name_cfg()
...