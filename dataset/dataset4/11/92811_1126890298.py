
# create the parsers action and add it to the positionals list
parsers_class = self._pop_action_class(kwargs, 'parsers')
action = parsers_class(option_strings=[], **kwargs)
self._subparsers._add_action(action)
