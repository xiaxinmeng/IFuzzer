s = "E-112233-555-11 | Bläh - Bläh"

expr = re.compile(r"(?P<p>[A-Z]{1}-[0-9]{0,}(-[0-9]{0,}(-[0-9]{0,})?)?)?(( [|] )?(?P<a>[\s\w]*)?)? - (?P<j>[\s\w]*)?",re.UNICODE)
res = re.match(expr,s)
a = (res.group('p'), res.group('a'), res.group('j'))
print(a)