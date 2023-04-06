import pathlib
from http.cookiejar import FileCookieJar

saved_cookies = pathlib.Path('my_cookies.txt')
jar = FileCookieJar(saved_cookies)