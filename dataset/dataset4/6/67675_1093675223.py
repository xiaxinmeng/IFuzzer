parser.add_subparser(dest='foo', action='append')
parser.parse_args('bar').__dict__ == {'foo': ['bar']}