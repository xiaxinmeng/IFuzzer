
from urllib.parse import urlparse
url1=urlparse('https://www.attacker.com/a/b')
url2=urlparse('https:///www.attacker.com/a/b')
url3=urlparse('https:/www.attacker.com/a/b')
url4=urlparse('https:\www.attacker.com/a/b')
print("Normal behaviour: HOSTNAME should be in netloc\n")
print(url1)
print("\nMishandling hostname and returning it as path\n")
print(url2)
print(url3)
print(url4)
