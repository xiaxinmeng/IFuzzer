class MyHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def add_argument(self, action):
        if action.dest != "SUPPRESS":
            super(RekallHelpFormatter, self).add_argument(action)


parser = ArguementParser(
   formatter_class=MyHelpFormatter)