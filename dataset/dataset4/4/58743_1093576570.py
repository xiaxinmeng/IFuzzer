from HTMLParser import HTMLParser
parser = process_html()
parser.feed('<a></a><script></script><meta><meta / ><body></body>')