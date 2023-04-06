p.add_argument('--file', type=open, default='/etc/passwd')
a = p.parse_args([])
a.file.read()