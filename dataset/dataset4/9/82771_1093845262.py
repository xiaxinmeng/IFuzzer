import argparse

parser = argparse.ArgumentParser()
single_group = parser.add_argument_group(title='single_group')
single_group.add_argument('--a', action='store_true')

mutex_group = parser.add_mutually_exclusive_group()
mutex_group.add_argument('--b', action='store_true')

nested_group = mutex_group.add_argument_group(title='nested_group')
nested_group.add_argument('--c', action='store_true')
nested_group.add_argument('--d', action='store_true')

parser.print_help()
print(parser.parse_args())