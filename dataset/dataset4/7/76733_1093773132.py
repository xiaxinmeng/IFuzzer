def my_add_argument(parser, *args, add_default=True, **kwargs):
    if add_default:
        help = kwargs.get('help','')
        help += ' (default: %(default)s)'
        kwargs['help'] = help
    return parser.add_argument(*args, **kwargs)