with open(os.path.expanduser('~/.pypirc'), 'w') as file:
    file.write(
"""[section]
key = value
""")