fp = open('/etc/issue')
with fp:
    print("first")
with fp:
    print("second")