FORM = cgi.FieldStorage()
for f in FORM:
	if f in ['uploaded_file']:
		uploadedFile = FORM[k]
		break