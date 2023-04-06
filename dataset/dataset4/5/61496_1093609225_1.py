for statement in user_input():
  if statement:
    exec(compile(statement, '<input>', 'single'))