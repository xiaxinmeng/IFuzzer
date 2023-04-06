class ReaderMapping(dict):
    def __init__(self):
        super().__init__({"abc": "xyz"})
        self.mode = "r"
        self.data = "123"
    def read(self, size):
        data = self.data
        self.data = ""
        return data

urlopen(Request("http://localhost/", headers={"Content-Length": 3}, data=ReaderMapping()))