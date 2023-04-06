# Could also be named use_accelerator to be less hostile-sounding.
def requires_accelerator(self, cls):
  if self.accelerated_module is None:
    raise SkipTest  # With proper message
  else:
    setattr(cls, self.module_name, self.accelerated_module)
    return cls