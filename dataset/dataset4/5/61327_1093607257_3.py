import tokenize

with open('example.py') as file: # opening a file encoded as UTF-8
	for token in tokenize.tokenize(file.readline):
		print(token)