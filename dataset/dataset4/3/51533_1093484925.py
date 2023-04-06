version = "2.7"
parser = argparse.ArgumentParser(
    description="My program XXX, version " + version)
parser.add_argument('-v', action='version', version=version)