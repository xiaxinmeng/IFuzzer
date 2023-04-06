
class GithubPath(pathlib.PurePosixPath):

  def __new__(cls, *args, **kwargs):
    print('New')
    return super().__new__(cls, *args, **kwargs)

  def __init__(self, *args, **kwargs):
    print('Init')
    super().__init__()
