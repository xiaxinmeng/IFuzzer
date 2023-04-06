spec = importlib.util.spec_from_file_location("target", "target.py")
imported_by_importlib = importlib.util.module_from_spec(spec)
spec.loader.exec_module(imported_by_importlib)