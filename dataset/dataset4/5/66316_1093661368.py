u = 'https://www.appeals2.az.gov/../Decisions/CR20130096OPN.pdf'
# Split the url and rejoin it, nuking any '/..' patterns at the
# beginning of the path.
s = urlsplit(u)
urlunsplit(s[:2] + (re.sub('^(/\.\.)+', '', s.path),) + s[3:])