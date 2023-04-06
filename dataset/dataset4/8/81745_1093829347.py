import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--mybool", type=bool)
parsed_args = parser.parse(["--mybool", "False"])