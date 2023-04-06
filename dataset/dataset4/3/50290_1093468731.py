class bdist_msi_patch_version(bdist_msi):
    """ MSI builder requires version to be in the x.x.x format """
    def run(self):
        def monkey_get_version(self):
            """ monkey patch replacement for metadata.get_version() that
                returns MSI compatible version string for bdist_msi
            """
            # get filename of the calling function
            if inspect.stack()[1][1].endswith('bdist_msi.py'):
                # strip revision from version (if any), e.g. 11.0.0-r31546
                return self.version.split('-')[0]
            else:
                return self.version