from HTMLParser import HTMLParser
HTMLParser().feed("<a onclick=foo({bar:42}); class=baz>")