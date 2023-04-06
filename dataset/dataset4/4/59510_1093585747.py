# Define a writable temp dir that will be used as cwd while running
# the tests. The name of the dir includes the pid to allow parallel
# testing (see the -j option).
TESTCWD = 'test_python_{}'.format(os.getpid())
...
with support.temp_cwd(TESTCWD, quiet=True):
    main()