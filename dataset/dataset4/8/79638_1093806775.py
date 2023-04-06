from urllib import robotparser

robots_url = "file:///tmp/empty.txt"

rp = robotparser.RobotFileParser()
print(robots_url)
rp.set_url(robots_url)
rp.read()
print( "fetch /", rp.can_fetch(useragent = "*", url = "/"))
print( "fetch /admin", rp.can_fetch(useragent = "*", url = "/admin"))