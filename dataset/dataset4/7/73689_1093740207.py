py_library(
  name = "foo", # abstract name
  imports = ".",
  srcs = ["pyfoo/foo.py"], # Which source files are in that library
)

py_test(
  name = "bartest",
  srcs = ["pyfoo/src/test/bar.py"], # The test script
  deps = ["foo"], # "Will import foo" -> import of foo's parent directory is added when executing test
)