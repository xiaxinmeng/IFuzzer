parser = argparse.ArgumentParser()
parser.add_argument('input', type=argparse.FileType())
arguments = parser.parse_args()

with arguments.input as f:
   assert arguments.input is f