class Junk:
    def __repr__(self):
        raise AttributeError('junk')

import logging; logging.warning('%r', Junk())
print('Done.')