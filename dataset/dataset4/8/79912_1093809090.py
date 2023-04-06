
def open(*urls, new=0, autoraise=True):
        ...
        browser = get(name)
        actions = [browser.open(url, new, autoraise) for url in urls]
        ...

# usage
open('http://example.com', 'http://example2.com')
