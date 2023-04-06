str = PyString_FromStringAndSize(
   NULL, size * nchannels * (len * outrate + inrate - 
1) / inrate);