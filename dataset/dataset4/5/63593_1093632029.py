extensions = [
    Extension("test_extension", ["test_extension.cpp"],
        include_dirs = [""],
        libraries = ["rt"],
        library_dirs = [""],
        )
]