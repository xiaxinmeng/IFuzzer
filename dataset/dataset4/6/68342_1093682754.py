from pathlib import Path
p = Path('/any/folder')
f = p / 'oldname'
f.rename('newname')