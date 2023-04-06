import itertools, sys
sys.stdout.writelines(itertools.repeat('""+', 2**17))
print('""')