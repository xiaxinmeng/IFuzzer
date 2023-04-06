if 'help' in kwargs:
            help = kwargs.pop('help')
            if help != SUPPRESS:
                choice_action = self._ChoicesPseudoAction(name, help)
                self._choices_actions.append(choice_action)