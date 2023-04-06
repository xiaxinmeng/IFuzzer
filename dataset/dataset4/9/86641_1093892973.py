import re

data = [
    '= hello =',
    'i am next line with <unk>',
]

pttn = re.compile(r'=.*=')
samples = filter(lambda sample: not pttn.match(sample), data)

pttn = re.compile(r'<unk>')
samples = map(lambda sample: pttn.sub('[unk]', sample), samples)

print(list(samples))