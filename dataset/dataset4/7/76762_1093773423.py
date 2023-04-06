import ConfigParser

tmpfile = "test.ini"
conf = ConfigParser.ConfigParser()
conf.read(tmpfile)
conf.set("section_a", "addr", "\"127.0.0.2\"")
cfgfile = open(tmpfile, 'w')
conf.write(cfgfile) 