
match = re.match('(?P<a>a)', 'a')
match.get('b')  # should return None
match.get(1)  # should return 'a'
'a' in match # True
'b' in match # False
