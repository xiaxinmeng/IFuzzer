agroup = subcmd_parser.add_mutually_exclusive_group()
agroup.add_argument('--a1', action='store_true', help='blah')
agroup.add_argument('--a2', action='store_true', help='blah')
agroup.add_argument('--a3', action='store_true', help='blah')

bgroup = subcmd_parser.add_mutually_exclusive_group()
bgroup.add_argument('--b1', action='store_true', help='blah')
bgroup.add_argument('--b2', action='store_true', help='blah')
bgroup.add_argument('--b3', action='store_true', help='blah')