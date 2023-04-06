parser.add_argument('COMMAND', help='command to run')
parser.add_argument('ARGUMENT', nargs='*', help='arguments to COMMAND')
parser.add_argument('-V', '--version', action='version', version=PROGRAM_NAME + ' ' + VERSION)