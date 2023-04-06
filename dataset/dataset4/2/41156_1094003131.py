import sgmllib, urllib, urlparse
from sgmllib import SGMLParser


if __name__ == "__main__":
    url = "http://www.cs.uvic.ca/~gshoja/"
    parser = SGMLParser()
    data = urllib.urlopen(url).read()