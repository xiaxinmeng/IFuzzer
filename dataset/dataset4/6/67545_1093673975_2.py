def convert_arg_line_to_args(self, arg_line):
    for arg in arg_line.split():
        yield arg