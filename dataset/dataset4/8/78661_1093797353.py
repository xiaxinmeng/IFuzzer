import bs4

html = '''<html><head><!fill in here--> <![end--><!-- start: SSI y-xtra-topspace.shtml --><!-- --></head><body></body></html>'''

soup = bs4.BeautifulSoup(html, 'html.parser')