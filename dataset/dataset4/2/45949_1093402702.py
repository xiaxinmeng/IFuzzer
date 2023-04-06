self.checkraises(OverflowError,
                             '\ta\n\tb', 'expandtabs', sys.maxint)