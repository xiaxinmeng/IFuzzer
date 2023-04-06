from distutils.core import setup
setup(name='my_package',
      package_dir={'my_package': ''},
      packages=['my_package', 'my_package.view'],
      package_data={'my_package': ['view/*.glade']}
)