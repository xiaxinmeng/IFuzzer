# test.py
import argparse

parser = argparse.ArgumentParser()
dbsettings = parser.add_argument_group('Database settings')
xdbgrp = dbsettings.add_mutually_exclusive_group(required=True)
xdbgrp.add_argument('--db-config')

grp = xdbgrp.add_argument_group(required=True)
grp.add_argument('--db-host')
grp.add_argument('--db-user')

xgrp = grp.add_mutually_exclusive_group()
xgrp.add_argument('--db-password')
xgrp.add_argument('--db-password-file')
parser.parse_args()