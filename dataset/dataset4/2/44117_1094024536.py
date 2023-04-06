env = Environment()
env.Replace(CCFLAGS=['-O0','-ggdb','-Wall','-ansi','-pedantic'])
env.SharedLibrary('spfuncs',['spfuncs.c'])