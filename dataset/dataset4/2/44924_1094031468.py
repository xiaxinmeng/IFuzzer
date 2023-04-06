a = "aa bbb cc D"
b = "aa czbb cc E"

sm = difflib.SequenceMatcher(None, a, b).get_opcodes()