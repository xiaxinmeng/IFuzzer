class MyFormatter(argparse.HelpFormatter):
    def __init__(self, prog):
        super(MyFormatter, self).__init__(prog, max_help_position=2000, width=2000)
        self._max_help_position = 2000
        self._action_max_length += 4