parser = make_parser()
parser.parse("file.xml")

parser.reset()

parser.feed("<doc/>")
parser.close()