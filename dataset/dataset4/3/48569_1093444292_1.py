import optparse
parser = optparse.OptionParser()
parser.add_option("--test",help="This does not work: é")
parser.parse_args()