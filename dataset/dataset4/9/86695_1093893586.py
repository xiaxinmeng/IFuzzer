
...
from setuptools import Extension
...
import setupext
...
jpypeLib = Extension(name='_jpype', **setupext.platform.Platform(
    include_dirs=[Path('native', 'common', 'include'),
                  Path('native', 'python', 'include'),
                  Path('native', 'embedded', 'include')],
    sources=[Path('native', 'common', '*.cpp'),
             Path('native', 'python', '*.cpp'),
             Path('native', 'embedded', '*.cpp')], platform=platform,
))
