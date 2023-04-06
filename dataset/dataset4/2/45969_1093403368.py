# head
python_build = os.path.isfile(os.path.join(project_base, "Modules",
                                           "Setup.local"))
# after revert
python_build = os.path.isfile(os.path.join(project_base, "Modules",
                                           "Setup.dist"))