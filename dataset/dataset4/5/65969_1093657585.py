def compile_script(script_name):
    py_compile.compile(script_name, doraise=True)
    if __debug__:
        compiled_name = script_name + 'c'
    else:
        compiled_name = script_name + 'o'
    return compiled_name