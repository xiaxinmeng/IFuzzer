import mock

arg = ['one']

test_function(arg)

# passes
test_function.assert_has_calls([mock.call(['one'])])

arg += ['two']

test_function(arg)

# fails, even though we just verified the first call above!
test_function.assert_has_calls([
    mock.call(['one']),
    mock.call(['one','two'])
])

# passes, even though we didn't make the exact same call twice!
test_function.assert_has_calls([
    mock.call(['one', 'two']),
    mock.call(['one', 'two'])
])