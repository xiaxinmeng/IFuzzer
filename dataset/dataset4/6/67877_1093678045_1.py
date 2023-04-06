s = 200_000_000 * 'a'
p = re.compile(r'.*?(?:bb)+')
p.match(s)  # <- measure this statement