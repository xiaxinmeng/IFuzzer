from distutils.sysconfig import parse_makefile, get_config_vars

config_vars = get_config_vars()
config_vars['CC'] = 'gcc-2.95'