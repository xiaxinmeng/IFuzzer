
import netrc
import os.path

netrc.netrc(os.path.expanduser('~/.netrc')).authenticators('api.github.com')
