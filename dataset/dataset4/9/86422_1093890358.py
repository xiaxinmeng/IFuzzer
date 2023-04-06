
str = re.sub('(=\w{3},\s[\w\d\s-]{9,11}\s[\d:]{8}\sGMT),', r'\1;', str)
