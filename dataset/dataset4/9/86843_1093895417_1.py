class ArgumentParserCustom(argparse.ArgumentParser):
    
    def convert_arg_line_to_args(self, arg_line):
    
        if (re.match(r'^[\s]*#', arg_line) or   # Look for any number of whitespace characters up to a `#` character
            re.match(r'^[\s]*$', arg_line)):  # Look for lines containing nothing or just whitespace
            return []
        else:
            return [arg_line]