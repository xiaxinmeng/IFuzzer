class foo:
    @staticmethod
    def bar():
        """
        >>> GLOBAL = 5; foo.bar()
        5
        """
        print(GLOBAL)