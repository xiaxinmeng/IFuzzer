with open(__file__) as f:
    src = f.read()
with open(__file__, 'w') as f:
    f.write('\n\n\n\n\n# Whoops! Wrong line!\n')
    f.write(src)
raise NotImplementedError('The prepended lines have confused you.')