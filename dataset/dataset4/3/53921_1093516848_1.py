exec(sample)
# output: un éléphant, deux éléphants, ...
exec(sampleb)
# output: un éléphant, deux éléphants, ...

module = BytesIO()
module.write(sampleb)
module.seek(0)

for line in tokenize(module.readline):
    print(tok_name[line.type], line)