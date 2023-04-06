
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", u"--file", dest="filename",
                  help="write to FILE. Default value %default",
                  metavar="FILE",
                  default=u"   ")

parser.add_option("-f", u"--   ", dest="filename",
                  help="write to FILE. Default value %default",
                  metavar="FILE",
                  default=u"   ")


(options, args) = parser.parse_args()
