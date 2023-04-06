auth = netrc.netrc(os.path.expanduser(r"~\.netrc"))
print(auth.__repr__())