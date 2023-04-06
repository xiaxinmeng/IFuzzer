import os
import gettext
import argparse

os.putenv('LANG', 'en_US')  # Just to make sure.
gettext.bindtextdomain('foo', '.')
gettext.textdomain('foo')

p = argparse.ArgumentParser()
p.add_argument('--foo', nargs=None)
p.parse_args()