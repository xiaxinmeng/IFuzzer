with open('/tmp/x.ssv', 'r') as f:
    f.readline()
    # imagine a library call boundary here
    if hasattr(f, 'reconfigure'):
        f.reconfigure(newline='\n')