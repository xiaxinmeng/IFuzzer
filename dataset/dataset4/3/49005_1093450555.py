base_dir = os.path.commonpath(paths)
rel_paths = [os.path.relpath(p, base_dir) for p in paths]