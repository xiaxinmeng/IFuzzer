class StreamArray(list):
    def __init__(self, generator):
        super().__init__()
        self.generator = generator
    def __iter__(self):
        return self.generator
    def __len__(self):
        return 1