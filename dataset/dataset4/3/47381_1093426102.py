fixer_pkg = os.path.relpath(self.fixer_dir,
os.path.join(os.path.dirname(__file__), '..'))
fixer_pkg = fixer_pkg.replace(os.path.sep, ".")