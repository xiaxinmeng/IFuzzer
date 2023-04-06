import robotparser
url = 'http://mueblesmoraleda.com' # whole site is password-protected.
parser = robotparser.RobotFileParser()
parser.set_url(url)
parser.read()	# Prompts for password