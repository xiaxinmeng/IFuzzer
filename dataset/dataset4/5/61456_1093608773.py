import encodings

aliases = encodings.aliases.aliases
more_aliases = {'ibm874'     : 'cp874',
                'iso_8859_11': 'cp874',
                'iso8859_11' : 'cp874',
                'windows_874': 'cp874',
               }
aliases.update(more_aliases)