import argparse

parser = argparse.ArgumentParser()
grp = parser.add_argument_group('Database settings')
grp.add_argument('--db-config')
xgrp = grp.add_argument_group()
xgrp.add_argument('--db-password')
parser.parse_args(['-h'])