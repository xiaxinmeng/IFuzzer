def test_cwd(arg0, arg_cwd):
    os.chdir('foo')  # Make sure we're in a different directory from arg0.
    p = subprocess.Popen([arg0, "-c",
                          "import os, sys; "
                          "sys.stdout.write(os.getcwd()); "
                          "sys.exit(47)"],
                          stdout=subprocess.PIPE,
                          cwd=arg_cwd)
    p.wait()
    print("stdout: " + p.stdout.read().decode("utf-8"))
    print("return_code: %s" % p.returncode)

python_path = os.path.realpath(sys.executable)
python_dir, python_base = os.path.split(python_path)
rel_python = os.path.join(os.curdir, python_base)

# Raises: WindowsError: [Error 2] The system cannot find the file specified
test_cwd(rel_python, python_dir)