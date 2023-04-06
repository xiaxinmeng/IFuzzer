if os.path.isfile(pathlib.Path(self.parent_dir).joinpath('gmon.out')):
  os.remove(pathlib.Path(self.parent_dir).joinpath('gmon.out'))