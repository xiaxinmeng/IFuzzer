
from urllib.request import urlopen



remote_urls = request.POST.getlist("source[]", [])
for remote_url in remote_urls:
    remote_image = urlopen(remote_url)

