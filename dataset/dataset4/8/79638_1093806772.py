rp = robotparser.RobotFileParser()
print (robotsurl)
rp.set_url(robotsurl)
rp.read()
print( "fetch /", rp.can_fetch(useragent = "*", url = "/"))
print( "fetch /admin", rp.can_fetch(useragent = "*", url = "/admin"))