import argparse
parser=argparse.ArgumentParser(prog='cli')
parser.add_argument('nodes')
sp=parser.add_subparsers()
p1 = sp.add_parser('list', description='Lists nodes in your current project')
p1.add_argument('-p','--projectid', action='store_true')
p1.add_argument('-o', '--org', action='store_true', help=' (For administrators only) Lists all the nodes in')
parser.parse_args()