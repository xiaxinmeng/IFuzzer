import argparse
parser = argparse.ArgumentParser(description="My parser")
parser.add_argument("--my_bool", type=bool)
cmd_line = ["--my_bool", "False"]
parsed_args = parser.parse(cmd_line)