sorted(tree, cmp=lambda x, y: 1 if x in tree[y] else -1 if y in tree[x] else 0)