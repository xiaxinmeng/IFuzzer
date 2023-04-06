import importlib.util as util
spec = util.find_spec('_testmultiphase')
spec.name = '_testmultiphase_with_bad_traverse'
m = spec.loader.create_module(spec)