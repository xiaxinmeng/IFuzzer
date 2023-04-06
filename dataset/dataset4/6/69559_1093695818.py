def list_submodules(package):
    # Ensure it is a package before loading or importing it
    for name in parent_packages:
        loader = pkgutil.find_loader(name)
        assert loader.is_package()
    # Could call importlib.import_module(), but this seemed easier because I already have the loader:
    package = loader.load_module(name)
    # The only reason I want to load the module:
    search_path = package.__path__
    return pkgutil.iter_modules(search_path)