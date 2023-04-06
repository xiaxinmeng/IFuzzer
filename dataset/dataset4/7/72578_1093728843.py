sopts = """-a "Do""This""Separate" """
resx = ["-a", '"Do"', 'ThisSeparate', ]
res=shlex.split(sopts,posix=False)