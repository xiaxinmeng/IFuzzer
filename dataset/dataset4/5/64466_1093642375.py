import os, tempfile
os.mkdir('parent')
os.chdir('parent')
t = tempfile.TemporaryDirectory(dir=".")
os.rename('../parent', '../parent2')
t.cleanup()