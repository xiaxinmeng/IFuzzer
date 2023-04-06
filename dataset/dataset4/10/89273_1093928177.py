class OneMetavarHelpFormatter(argparse.HelpFormatter):
    """A formatter that avoids repeating action argument metavars.
    """
    def _format_action_invocation(self, action):
        "Format action help without repeating the argument metavar"
        if not action.option_strings or action.nargs == 0:
            return super()._format_action_invocation(action)

        default = self._get_default_metavar_for_optional(action)
        args_string = self._format_args(action, default)
        return ', '.join(action.option_strings) + ' ' + args_string