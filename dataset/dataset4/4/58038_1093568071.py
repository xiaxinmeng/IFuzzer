def custom_handler(error):
    print(error.args,
          (error.start, error.end, error.reason))
    return b'?'.decode(), error.end

import codecs
codecs.register_error('custom', custom_handler)
b'\x80\xd0'.decode('utf-8', 'custom')