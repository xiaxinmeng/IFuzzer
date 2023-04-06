
def with_global_before():
    global bar
    with open('/etc/hosts') as bar:
        ...
