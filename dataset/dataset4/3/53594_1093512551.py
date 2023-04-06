parser = argparse.ArgumentParser()	
parser.add_argument('--foo', nargs=2, metavar=('X','Y','Z'))
parser.parse_args(['-h'])