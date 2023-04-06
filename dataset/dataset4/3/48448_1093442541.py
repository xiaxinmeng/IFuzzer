f = r'V:\pdfs\boson1.pdf'
same = os.path.samefile(f, f)
print(same) # expected True; got False