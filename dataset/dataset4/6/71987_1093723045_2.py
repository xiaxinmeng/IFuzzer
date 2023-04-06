# Without the second level of brackets, this raises a "multiple repeat" error
chunk_re = br'(?: (?: [^A-Za-z0-9+/=]* [A-Za-z0-9+/=] ){4} )*'