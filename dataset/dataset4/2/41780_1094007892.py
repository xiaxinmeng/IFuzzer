class Quit:
    def __repr__(self):
        import sys
        sys.exit(0)
quit = Quit()
del Quit