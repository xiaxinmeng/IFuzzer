def _format_option_with_args(self, option_string, args_string):
        if option_string.startswith('--'):
            return '%s %s' % (option_string, args_string)
        return '%s' % option_string