width = min(80, shutil.get_terminal_size().columns - 2)
formatter_class = lambda prog: argparse.RawDescriptionHelpFormatter(prog, width=width)