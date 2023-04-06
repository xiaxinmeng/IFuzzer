from xml.parsers import expat

xml = "<?xml version='1.0' encoding='iso8859-1'?><s>%s</s>" % ('a' * 10000)
#xml = "<?xml version='1.0'?><s>%s</s>" % ('a' * 10000)

def handler(text):
  raise Exception

parser = expat.ParserCreate()
parser.CharacterDataHandler = handler


try:
  parser.Parse(xml)
except:
  pass


 	  	 
