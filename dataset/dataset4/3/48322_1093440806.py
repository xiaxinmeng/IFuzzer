from lib2to3.refactor import RefactoringTool, get_fixers_from_package
fixers = get_fixers_from_package('lib2to3.fixes')
options = dict(doctests_only=False, fix=[], list_fixes=[], 
               print_function=False, verbose=False,
               write=True)
r = RefactoringTool(fixers, options)
r.refactor(self.updated_files)