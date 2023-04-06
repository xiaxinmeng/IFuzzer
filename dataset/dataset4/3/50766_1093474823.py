import ConfigParser
import tempfile

file = tempfile.TemporaryFile(mode='rw+b')
file.write("[s]\nf=%%(b)s\n")
file.seek(0)
config = ConfigParser.ConfigParser()

config.readfp(file)