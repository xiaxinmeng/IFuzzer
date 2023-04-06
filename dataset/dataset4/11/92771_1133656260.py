shutils.rmtree(epath.Path('gs://bucket/a'))  # Fail
shutils.rmtree(universal_pathlib.UPath('s3://bucket/a'))  # Fail
shutils.copy(zipfile.Path('x.zip', 'file.txt'), 'dst/file.txt')  # Fail