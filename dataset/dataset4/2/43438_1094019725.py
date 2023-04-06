def print_help(self, file=None):
    if file is None:
        file = sys.stdout
    file.write(self.format_help().encode(file.encoding,
'replace'))