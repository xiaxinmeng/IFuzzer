import argparse
# create parent parser
parent_parser = argparse.ArgumentParser(add_help = False)
# create group for its arguments
global_group = parent_parser.add_argument_group("global arguments")
global_group.add_argument("--global-arg1")
global_group.add_argument("--global-arg2")
mutex_group = global_group.add_mutually_exclusive_group()
mutex_group.add_argument("--mutex-arg1")
mutex_group.add_argument("--mutex-arg2")
# create child parser
child_parser = argparse.ArgumentParser(parents = [parent_parser])
child_parser.add_argument("--child-arg1")
child_parser.add_argument("--child-arg2")
print("="*100)
parent_parser.print_help()
print("="*100)
child_parser.print_help()