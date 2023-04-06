from distutils.core import setup, Extension
setup(name='testpyd', scripts = ["testpyd_postinstall.py"],
    ext_modules=[Extension('testpyd', ['testpyd.c'],)],
    options = {"bdist_wininst": {"install_script": 
        "testpyd_postinstall.py", "user_access_control": "auto"},})