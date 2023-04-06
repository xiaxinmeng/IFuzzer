from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write to FILE. Default value %default", metavar="FILE", default="早上好")