s = re.escape(user_input)
s = re.sub(u'n|ñ', u'[n|ñ]')
matches = list(re.findall(s, data, re.IGNORECASE|re.UNICODE))