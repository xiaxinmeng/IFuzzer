
import sys
from os import getcwd, chdir
from runpy import run_path


def smoke_test(script, *args):
    old_argv = list(sys.argv)
    del sys.argv[:]
    sys.argv.append(script)
    sys.argv.extend(args)

    old_modules = dict(sys.modules)
    old_meta_path = list(sys.meta_path)
    old_cwd = getcwd()

    try:
        return run_path(script, run_name="__main__")
    except SystemExit as e:
        if e.code:
            print("Test did not exit successfully")
    finally:
        del sys.argv[:]
        sys.argv.extend(old_argv)

        sys.modules.clear()
        sys.modules.update(old_modules)

        del sys.meta_path[:]
        sys.meta_path.extend(old_meta_path)
        chdir(old_cwd)


smoke_test("script.py")

smoke_test("script.py")
