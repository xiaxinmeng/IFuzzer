cgi_file1 = """\
#!%s
..."""

with open(self.file1_path, 'w') as file1:
    file1.write(cgi_file1 % sys.executable)