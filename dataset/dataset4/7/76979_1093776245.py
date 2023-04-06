open_file = open("file.txt", "r+b")
file_map = mmap.mmap(open_file, 0)
file_map.seek(offset)
file_map.write("foobar") # success
file_map.flush() # success
file_map.flush(offset, len("foobar")) # Fails with "errno 22"