from urllib.request import urlopen
url = 'http://worldtimeapi.org/api/timezone/etc/UTC.txt'
with urlopen(url) as request:
    for line in request:
        line = line.decode('utf-8')
        if line.startswith('datetime'):
            print(line)