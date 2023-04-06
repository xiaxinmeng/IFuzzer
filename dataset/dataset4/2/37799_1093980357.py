def bs(input):
	pattern = re.compile('\"\+\"')
	match = lambda x: ""
	massage = copy.copy(BeautifulSoup.MARKUP_MASSAGE)
	massage.extend([(pattern, match)])
	return BeautifulSoup(input, markupMassage=massage)