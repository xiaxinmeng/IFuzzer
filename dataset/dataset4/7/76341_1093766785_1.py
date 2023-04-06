with open(in_path) as in_file, lzma.open(out_path, 'w') as out_file:
    shutil.copyfileobj(in_path, out_file)