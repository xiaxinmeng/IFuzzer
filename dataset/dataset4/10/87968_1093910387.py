from music21 import corpus
# suggest using a unique name each attempt
lc = corpus.corpora.LocalCorpus(name='bpo-investigation')
# point to the directory of files I committed to my fork for this investigation
lc.addPath('/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/music21/bpo-files')
# parse the files using multiprocessing
# calls music21.metadata.bundles.MetadataBundle.addFromPaths()
# which calls music21.metadata.caching.process_parallel()
lc.save()

# CTRL-C to recover from seg fault
# then, wipe out the entries in .music21rc so that you can cleanly reproduce again
from music21 import environment
us = environment.UserSettings()
us['localCorporaSettings'] = {}
quit()