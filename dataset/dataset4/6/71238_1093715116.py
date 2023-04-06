from pip_tkinter._vendor import pkg_resources
installed_packages = [p.project_name for p in pkg_resources.working_set]