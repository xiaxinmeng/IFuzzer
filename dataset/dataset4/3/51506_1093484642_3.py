a = [{'k': 'foo'}, {'k': 'bar'}]
a.sort(key=lambda x: x['k'])
# a is now [{'k': 'bar'}, {'k': 'foo'}]