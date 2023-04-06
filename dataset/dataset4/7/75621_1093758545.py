# Same to sysconfig.get_path('purelib', os.name+'_user')
def _get_path(userbase):
    version = sys.version_info

    if os.name == 'nt':
        return f'{userbase}\\Python{version[0]}{version[1]}\\site-packages'

    if sys.platform == 'darwin' and sys._framework:
        return f'{userbase}/lib/python/site-packages'