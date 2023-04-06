from os import getcwd, listdir, rename
import re

for n in listdir(p := f"{getcwd()}\\{input('Folder: ')}\\"):
    [rename(f'{p}{n}', f"{p}{''.join([w[:3] if len(w) > 3 else w for w in re.split('[-_. ]', n)[:-1]])}.{n.split('.')[-1]}")]