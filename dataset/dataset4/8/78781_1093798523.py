
parser = et.XMLParser(target=et.TreeBuilder())
parser.parser.CommentHandler = myCommentHandler
for event, elem in et.iterparse(fh, parser=parser):
    ...
