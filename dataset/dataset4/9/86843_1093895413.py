import argparse
import re


class ArgumentParserCustom(argparse.ArgumentParser):
    
    def convert_arg_line_to_args(self, arg_line):
    
        if re.match(r'(\s+)?#', arg_line):  # Look for any number of whitespace characters up to a `#` character
            return ['']
        else:
            return [arg_line]