from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlretrieve

with ThreadPoolExecutor(max_workers=3) as executor:
    url = 'http://www.{site}.org/'
    for site in ('perl', 'python', 'jython', 'pypy'):
        future = executor.submit(urlretrieve, url.format(site=site), site)