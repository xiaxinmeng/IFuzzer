from difflib import SequenceMatcher

a = 'ab'*400                                                                                    
b = 'ba'*400

for i in range(1, 400):
    diff_ratio = SequenceMatcher(None, a=a[:i], b=b[:i]).ratio()
    print('%3.i %.2f' % (i, diff_ratio), end=' ')
    not i % 10 and print('')