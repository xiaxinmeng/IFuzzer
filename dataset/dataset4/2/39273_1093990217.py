import ConfigParser
import sys

conf = ConfigParser.ConfigParser()
conf.add_section("sect")
conf.set("sect","option",2)
conf.write(sys.stderr)
conf.get("sect","option")
#----- END TEST 