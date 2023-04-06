if not result and sys.platform == 'darwin':
     # nl_langinfo can return an empty string
     # when the setting has an invalid value.
     # Default to UTF-8 in that case because
     # UTF-8 is the default charset on OSX and
     # returning nothing will crash the
     # interpreter.
     result = 'UTF-8'