spec = PathFinder.find_spec("_bootstrap",importlib.__path__)
source_bootstrap = type(sys)("_bootstrap");
spec.loader.exec_module(source_bootstrap);
source_bootstrap.__name__ = "importlib._bootstrap";    
new_sys = copy_module(sys)

new_sys.path_hooks = []
new_sys.meta_path = []
new_sys.modules = {
    "importlib._bootstrap":source_bootstrap,
    "importlib._bootstrap_external":importlib._bootstrap_external,
}
b.__import__ = source_bootstrap.__import__
source_bootstrap._install(new_sys,_imp)
dct["__file__"]=__file__
exec("open(__file__)",dct)