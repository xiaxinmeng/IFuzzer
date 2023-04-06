import urllib.robotparser
import urllib.request
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'MyUa/0.1')]
urllib.request.install_opener(opener)
rp = urllib.robotparser.RobotFileParser('http://localhost:9999')
rp.read()