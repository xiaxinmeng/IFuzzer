try:
     import rlcompleter,readline
except ImportError:

     pass    
else:
     readline.set_history_length(1000)
     # parse and bind all these:
     rlcmds = ['tab: complete',
               r'"\M-p": history-search-backward',
               r'"\M-n": history-search-forward',
               r'"\C-p": history-search-backward',
               r'"\C-n": history-search-forward',
               r'"\e[A": history-search-backward',
               r'"\e[B": history-search-forward',
               'set show-all-if-ambiguous on',
               ]       
     map(readline.parse_and_bind,rlcmds)
