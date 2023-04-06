from distutils.core import setup, Extension

if os.name == 'posix':
	CXX_libraries = ['stdc++','m']
else:
	CXX_libraries = []


setup(name="pycxx_demo", version="1.0",
	ext_modules=
		[Extension(
			"example",
			sources = [
				"Demo/example.cxx",
				"Demo/python.cxx",
				"Demo/range.cxx",
				"Demo/rangetest.cxx",
			
	"Src/cxx_extensions.cxx",
				"Src/cxxextensions.c",
				"Src/cxxsupport.cxx",
			
	"Src/IndirectPythonInterface.cxx" ],
			include_dirs = [ ".", "Demo" ],
			libraries = CXX_libraries
			)
		]
	)