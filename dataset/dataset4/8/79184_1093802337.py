def read_venv_scheme(env_dir):
    with open(os.path.join(env_dir, 'pyvenv.cfg')) as f:
        for line in f:
            key, value = (p.strip() for p in line.split('='))
            if key == 'scheme':
                return value

def get_venv_environ_patch(env_dir):
    scheme = read_venv_scheme(env_dir)
    bin_dir = sysconfig.get_path('scripts', scheme=scheme, expand=False).format(base=env_dir)
    return {'VIRTUAL_ENV': env_dir, 'PATH': bin_dir}