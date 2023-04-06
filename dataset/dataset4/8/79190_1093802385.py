
# -*- coding: utf-8 -*-

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='foo help', choices=[u"早上好", u"早上好 早上好"])
args = parser.parse_args()

