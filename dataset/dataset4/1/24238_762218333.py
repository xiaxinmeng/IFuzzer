
IGNORE = {
    '__pycache__',
    'site-packages',

    # Helper modules for public module
    # (ex: _osx_support is used by sysconfig)
    '_aix_support',
    '_collections_abc',
    '_compat_pickle',
    '_compression',
    '_markupbase',
    '_osx_support',
    '_sitebuiltins',
    '_strptime',
    '_threading_local',
    '_weakrefset',

    # Used to bootstrap setup.py
    '_bootsubprocess',

    # test modules
    'test',
    '__phello__.foo',

    # pure Python implementation
    '_py_abc',
    '_pydecimal',
    '_pyio',
}
