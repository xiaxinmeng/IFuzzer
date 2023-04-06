class OneList:

    def __len__(self):
        # this won't be checked by
        # PySequence_Fast and several
        # over C API calls
        return 1

    def __getitem__(self, x):
        # called indefinitely by
        # i.e., PySequence_Fast
        return 1