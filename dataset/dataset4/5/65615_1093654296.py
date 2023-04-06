parser = argparse.ArgumentParser()
parser.add_argument('somebytes', type=bytes, help='i want some bytes')
parser.parse_args()