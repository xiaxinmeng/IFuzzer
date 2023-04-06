test = TestClass(root)  # this creates a zipfile handle  (an instance of zipfile.ZipFile) at test.zip_file

files = test.iter_dir()  # this creates multiple instances of zipfile.Path() as part of the list comprehension and these are deferenced afterwards. I found that test.zip_file.fp is closed after this line executes, which to me suggests that the closing of the zipfile.Path also closes the zipfile.ZipFile that was used to create the zipfile.Path.

test.read(files[0])  # this should in theory try to read from the test.zip_file for the first time, but fails because it is closed as per the above.