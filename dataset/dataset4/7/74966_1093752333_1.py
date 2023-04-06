def create_venv(d, pypath=None):
    command = ['virtualenv', d]
    if pypath:
        command.extend(['-p', pypath])
    subprocess.call(command)


@contextmanager
def venv(d):
    if os.path.exists(os.path.join(d, 'bin')):  # no cov
        venv_exe_dir = os.path.join(d, 'bin')
    elif os.path.exists(os.path.join(d, 'Scripts')):
        venv_exe_dir = os.path.join(d, 'Scripts')
    else:
        raise OSError('Unable to locate executables directory.')

    old_path = os.environ['PATH']
    os.environ['PATH'] = '{}{}{}'.format(venv_exe_dir, os.pathsep, old_path)
    yield
    os.environ['PATH'] = old_path


def test_venv():
    with temp_chdir() as d:
        d = os.path.join(d, 'test_env')
        create_venv(d)
        global_python = get_python_path()
        print('PATH', os.environ['PATH'][:140])

        with venv(d):
            print('PATH', os.environ['PATH'][:140])
            venv_python = get_python_path()