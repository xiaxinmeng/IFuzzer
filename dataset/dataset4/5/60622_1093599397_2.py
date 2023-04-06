if action.choices is not None and value not in action.choices:
  msg = "invalid choice: %r (choose from %r)" % (value, action.choices)
  raise ArgumentError(action, msg)