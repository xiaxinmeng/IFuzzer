# Force g++ for linking
import distutils.sysconfig
old_customize_compiler = distutils.sysconfig.customize_compiler
def customize_compiler(compiler):
    old_customize_compiler(compiler)
    if compiler.compiler_type == 'mingw':
       compiler.set_executables(linker_so='g++ -mno-cygwin -shared')
distutils.sysconfig.customize_compiler = customize_compiler