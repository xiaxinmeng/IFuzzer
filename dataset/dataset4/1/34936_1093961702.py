import md5, sha
digests = { 'md5': md5, 'sha': sha } # using globals() is ugly
digest = sock.recv(digests[mdalg].digestsize)