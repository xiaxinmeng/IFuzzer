import sys, types, os;p = os.path.join(sys._getframe(1).f_locals['sitedir'], *('mpl_toolkits',));ie = os.path.exists(os.path.join(p,'__init__.py'));m = not ie and sys.modules.setdefault('mpl_toolkits', types.ModuleType('mpl_toolkits'));mp = (m or []) and m.__dict__.setdefault('__path__',[]);(p not in mp) and mp.append(p)