def _parse_cmdl(cmdl):
    parser = argparse.ArgumentParser()
    parser.add_argument("outdata", help="Path to output data file")
    parser.add_argument("plotTimes", nargs='*', help="Times to plot")
    parser.add_argument("outplot", help="Path to output plot file")
    return parser.parse_args(cmdl)