def traverse(path, visit):
    for child in path.iterdir():
        if child.is_dir():
            traverse(path, visit)
        else:
            visit(child)