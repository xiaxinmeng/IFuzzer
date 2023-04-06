AddressFamily = IntEnum('AddressFamily',
           {name: value for name, value in _moduledict.items()
            if name.startswith('AF_')})