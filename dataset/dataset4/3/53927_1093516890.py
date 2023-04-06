from django.test.client import Client
c = Client()
response = c.post(logindir, loginvars)
response = c.get(getdir)