from Cookie import BaseCookie
cookie = BaseCookie('asd={"asd"}; my-real-cookie=stuff i care about; blah=blah')
assert 'my-real-cookie' in cookie  # False