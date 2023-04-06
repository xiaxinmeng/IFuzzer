self.metadata = DistributionMetadata()
method_basenames = dir(self.metadata) + \
                    ['fullname', 'contact', 'contact_email']

for basename in method_basenames:
    method_name = "get_" + basename
    setattr(self, method_name, getattr(self.metadata, method_name))