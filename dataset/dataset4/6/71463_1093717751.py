loader = (importlib.machinery.SourceFileLoader, importlib.machinery.SOURCE_SUFFIXES)
sys.meta_path.append(importlib.machinery.FileFinder('/', loader))