while true:
   try:
      myParser.feed(data)
      break
   except SGMLCatcheableParseError:
      exc_value = sys.exc_info()[1]
      data = data[exc_value:]
      continue