import Cookie
from os import environ as env

C = Cookie.SimpleCookie()
C["CUX2"] = 123
C["CUX2"]['expires'] = 60*60*60