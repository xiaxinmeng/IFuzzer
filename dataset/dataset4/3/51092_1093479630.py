warnings.filterwarnings(
    'ignore',
    message='BaseException.message has been deprecated as of Python 2.6',
    category=DeprecationWarning,
    module=r'twisted\.conch\.ssh\.filetransfer')