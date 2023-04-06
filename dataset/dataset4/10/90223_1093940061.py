import re
pattern_email      = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,3}"
with open("res.html","r",encoding="utf-8") as FF:
	TEXT = FF.read()
matched_email          = re.findall(pattern_email,TEXT)