parser.add_argument('-p', '--preload', help='preload asset', action=AppendWithSwitchAction, metavar='NAMESPACE')

parser.add_argument('-f', '--file', help='preload file', action=AppendWithSwitchAction, metavar='FILE', dest='preload')