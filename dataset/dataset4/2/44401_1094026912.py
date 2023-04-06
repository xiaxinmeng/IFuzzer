from optparse import OptionParser

def process_options():
    global options, args, parser
    parser = OptionParser()

    parser.add_option("--test", action="store_true")
    parser.add_option("-m", metavar="COMMENT", dest="comment", default=None)
    (options, args) = parser.parse_args()
    return

process_options()