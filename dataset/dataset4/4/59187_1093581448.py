i = ImpImporter(path=vcs.__path__[0])
sys.path_importer_cache.setdefault(vcs.__path__[0], i)