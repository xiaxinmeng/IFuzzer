
#!/usr/bin/env python
''' Installation script that breaks '''

from distutils.command import install
from distutils.core import setup

class installer(install.install):
    def run(self):
        import setuptools
        install.install.run(self)


setup(name='test',
      cmdclass = dict(install=installer)
     )

