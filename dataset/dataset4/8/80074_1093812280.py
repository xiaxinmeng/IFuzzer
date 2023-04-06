#START
from distutils.command import build_ext

def get_export_symbols(self, ext):
    parts = ext.name.split(".")
    print('parts', parts)
    if parts[-1] == "__init__":
        initfunc_name = "PyInit_" + parts[-2]
    else:
        initfunc_name = "PyInit_" + parts[-1]

build_ext.build_ext.get_export_symbols = get_export_symbols
#END