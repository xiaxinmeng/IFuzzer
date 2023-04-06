# We must close the scandir() object before proceeding to
# avoid exhausting file descriptors when globbing deep trees.
with scandir(parent_path) as scandir_it:
    entries = list(scandir_it)
for entry in entries:
    ...