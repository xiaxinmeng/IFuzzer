from email.parser import Parser
BLOCKSIZE = 8192
s = 'From: <e@example.com>\nFoo: '
s += 'x' * ((-len(s) - 1) % BLOCKSIZE) + '\rBar: '
s += 'y' * ((-len(s) - 1) % BLOCKSIZE) + '\x85Baz: '
s += 'z' * ((-len(s) - 1) % BLOCKSIZE) + '\n\n'
print(Parser().parsestr(s).keys())