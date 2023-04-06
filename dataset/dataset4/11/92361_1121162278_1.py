
unsafe_env = dict(os.environ)
unsafe_env.pop("PYTHONSAFEPATH", "")
subprocess.run(["/usr/bin/app"], env=unsafe_env)
