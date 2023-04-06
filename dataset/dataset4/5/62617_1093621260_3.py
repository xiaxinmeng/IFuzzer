from urllib.request import DEFAULT_TIMEOUT, urlopen

def my_open(url, timeout=None):
    my_timeout = DEFAULT_TIMEOUT if timeout is None else timeout
    return urlopen(url, timeout=my_timeout)