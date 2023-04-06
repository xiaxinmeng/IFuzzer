EXTRA_INSTALL_SCHEMES = {
    'vendor': {
        'stdlib': '{installed_base}/{platlibdir}/python{py_version_short}',
        'platstdlib': '{platbase}/{platlibdir}/python{py_version_short}',
        'purelib': '{base}/lib/python{py_version_short}/vendor-packages',
        'platlib': '{platbase}/{platlibdir}/python{py_version_short}/vendor-packages',
        'include':
            '{installed_base}/include/python{py_version_short}{abiflags}',
        'platinclude':
            '{installed_platbase}/include/python{py_version_short}{abiflags}',
        'scripts': '{base}/bin',
        'data': '{base}',
    },
}

EXTRA_SITE_INSTALL_SCHEMES = [
    'vendor',
]