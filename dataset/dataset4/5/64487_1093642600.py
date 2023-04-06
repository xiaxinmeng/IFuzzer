p = HTMLParser()
p.handle_data = lambda x: sys.stdout.write(x)
p.feed('<p>&#foo;</p>')