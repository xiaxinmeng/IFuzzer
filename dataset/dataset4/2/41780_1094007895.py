class quit:
    def __repr__(self):
        return "Type quit() to exit the interpreter"
    def __call__(self):
        sys.exit()