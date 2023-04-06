env = os.environ.copy()
env['LC_ALL'] = 'C'
process = subprocess.Popen([executable, '-ia'], stderr=subprocess.DEVNULL)
...