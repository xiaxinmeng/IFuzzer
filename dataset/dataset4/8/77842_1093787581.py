import urllib.request
req = urllib.request.Request('http://httpleak.gypsyengineer.com/redirect.php?url=http://headers.gypsyengineer.com')
req.add_header('Authorization', 'Basic YWRtaW46dGVzdA==')
req.add_header('Cookie', 'This is only for httpleak.gypsyengineer.com');
with urllib.request.urlopen(req) as f:
  print(f.read(2048).decode("utf-8"))