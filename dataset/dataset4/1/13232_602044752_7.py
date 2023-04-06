
def with_global_after():
    with open('/etc/hosts') as bar:
        ...
    global bar
