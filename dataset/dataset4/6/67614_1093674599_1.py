class install1(install):
    sub_commands = install.sub_commamnds

setup(name='bug', cmdclass={'install': install1})