class RawDescriptionHelpFormatterMaxTextWidth80(argparse.RawDescriptionHelpFormatter):
        """Set maximum text width = 80."""

        def __init__(self, prog):
            width = min(80, shutil.get_terminal_size().columns - 2)
            argparse.RawDescriptionHelpFormatter.__init__(self, prog, width=width)